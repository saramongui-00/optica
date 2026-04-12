import json
import os
from typing import Optional, List
from datetime import datetime
import redis.asyncio as redis
from models.appointment import Appointment

class AppointmentRepository:
    def __init__(self):
        self.redis_client = redis.from_url(
            os.getenv("REDIS_URL", "redis://localhost:6379"),
            decode_responses=True
        )

    def _to_dict(self, appointment: Appointment) -> dict:
        data = appointment.model_dump()
        
        # Convertir fechas a string ISO de forma segura
        if data.get('date') and hasattr(data['date'], 'isoformat'):
            data['date'] = data['date'].isoformat()
        elif data.get('date') and isinstance(data['date'], str):
            pass  # Ya es string, no hacer nada
        
        if data.get('time') and hasattr(data['time'], 'isoformat'):
            data['time'] = data['time'].isoformat()
        elif data.get('time') and isinstance(data['time'], str):
            pass
        
        if data.get('createdAt') and hasattr(data['createdAt'], 'isoformat'):
            data['createdAt'] = data['createdAt'].isoformat()
        
        if data.get('updatedAt') and hasattr(data['updatedAt'], 'isoformat'):
            data['updatedAt'] = data['updatedAt'].isoformat()
        
        # Convertir patient a JSON string
        if data.get('patient') and isinstance(data['patient'], dict):
            data['patient'] = json.dumps(data['patient'])
        
        return data

    async def save(self, appointment: Appointment) -> str:
        appointment_id = await self.redis_client.incr("appointment:next_id")
        appointment.id = str(appointment_id)
        
        key = f"appointment:{appointment_id}"
        await self.redis_client.hset(key, mapping=self._to_dict(appointment))
        
        # Asegurar que date es string antes de fromisoformat
        date_str = appointment.date
        if hasattr(date_str, 'isoformat'):
            date_str = date_str.isoformat()
        
        date_ts = int(datetime.fromisoformat(date_str).timestamp())
        await self.redis_client.zadd("appointments_by_date", {str(appointment_id): date_ts})
        
        return str(appointment_id)

    async def find_by_id(self, appointment_id: str) -> Optional[dict]:
        key = f"appointment:{appointment_id}"
        data = await self.redis_client.hgetall(key)
        if not data:
            return None
        if data.get('patient'):
            data['patient'] = json.loads(data['patient'])
        data["id"] = appointment_id
        return data

    async def find_by_date(self, date_str: str) -> List[dict]:
        start_ts = int(datetime.fromisoformat(f"{date_str}T00:00:00").timestamp())
        end_ts = int(datetime.fromisoformat(f"{date_str}T23:59:59").timestamp())
        
        appointment_ids = await self.redis_client.zrangebyscore(
            "appointments_by_date", min=start_ts, max=end_ts
        )
        
        appointments = []
        for aid in appointment_ids:
            appt_data = await self.redis_client.hgetall(f"appointment:{aid}")
            if appt_data:
                if appt_data.get('patient'):
                    appt_data['patient'] = json.loads(appt_data['patient'])
                appt_data["id"] = aid
                appointments.append(appt_data)
        return appointments

    async def find_by_patient_document(self, document: str) -> List[dict]:
        keys = await self.redis_client.keys("appointment:*")
        keys = [k for k in keys if k != "appointment:next_id"]
        appointments = []
        for key in keys:
            appt_data = await self.redis_client.hgetall(key)
            if appt_data and appt_data.get("patient"):
                patient = json.loads(appt_data["patient"]) if isinstance(appt_data["patient"], str) else appt_data["patient"]
                if patient.get("document") == document:
                    appointment_id = key.split(":")[1]
                    appt_data["id"] = appointment_id
                    appointments.append(appt_data)
        return appointments

    async def update(self, appointment_id: str, data: dict) -> bool:
        key = f"appointment:{appointment_id}"
        exists = await self.redis_client.exists(key)
        if not exists:
            return False
        await self.redis_client.hset(key, mapping=data)
        return True

    async def update_state(self, appointment_id: str, state: str) -> bool:
        key = f"appointment:{appointment_id}"
        exists = await self.redis_client.exists(key)
        if not exists:
            return False
        
        await self.redis_client.hset(key, mapping={"state": state})
        return True

    async def delete(self, appointment_id: str) -> bool:
        key = f"appointment:{appointment_id}"
        deleted = await self.redis_client.delete(key)
        return deleted > 0

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[dict]:
        keys = await self.redis_client.keys("appointment:*")
        keys = [k for k in keys if k != "appointment:next_id"]
        
        start = skip
        end = skip + limit - 1
        paginated_keys = keys[start:end] if start < len(keys) else []
        
        appointments = []
        for key in paginated_keys:
            appointment_data = await self.redis_client.hgetall(key)
            if appointment_data:
                if appointment_data.get('patient'):
                    appointment_data['patient'] = json.loads(appointment_data['patient'])
                appointment_id = key.split(":")[1]
                appointment_data["id"] = appointment_id
                appointments.append(appointment_data)
        
        return appointments
    
    async def find_by_date_and_time(self, date_str: str, time_str: str) -> Optional[dict]:
        """Buscar cita por fecha y hora exacta usando el índice"""
        from datetime import datetime
        start_ts = int(datetime.fromisoformat(f"{date_str}T00:00:00").timestamp())
        end_ts = int(datetime.fromisoformat(f"{date_str}T23:59:59").timestamp())
        appointment_ids = await self.redis_client.zrangebyscore(
            "appointments_by_date", min=start_ts, max=end_ts
        )
        for aid in appointment_ids:
            appt_data = await self.redis_client.hgetall(f"appointment:{aid}")
            if appt_data and appt_data.get("time") == time_str:
                return appt_data
        return None
    
    async def exists_by_date_and_time(self, date_str: str, time_str: str) -> bool:
        """Verifica si ya existe una cita en esa fecha y hora"""
        keys = await self.redis_client.keys("appointment:*")
        for key in keys:
            if key == "appointment:next_id":
                continue
            cita = await self.redis_client.hgetall(key)
            if cita and cita.get("date") == date_str and cita.get("time") == time_str:
                return True
        return False
    
    async def create_if_not_exists(self, appointment: Appointment) -> tuple[bool, str]:
        """Crea la cita solo si no existe otra con misma fecha y hora"""
        # Usar una clave única compuesta por fecha+hora
        unique_key = f"appointment:lock:{appointment.date}:{appointment.time}"
        
        # Intentar crear la clave (solo si no existe)
        created = await self.redis_client.setnx(unique_key, "locked")
        
        if not created:
            return False, "Ya existe una cita en ese horario"
        
        # Si logramos el lock, crear la cita
        appointment_id = await self.redis_client.incr("appointment:next_id")
        appointment.id = str(appointment_id)
        
        key = f"appointment:{appointment_id}"
        await self.redis_client.hset(key, mapping=self._to_dict(appointment))
        
        # Índice por fecha
        date_ts = int(datetime.fromisoformat(appointment.date).timestamp())
        await self.redis_client.zadd("appointments_by_date", {str(appointment_id): date_ts})
        
        # Liberar el lock después de 5 segundos
        await self.redis_client.expire(unique_key, 5)
        
        return True, str(appointment_id)