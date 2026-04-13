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

    def _to_redis_dict(self, appointment: Appointment) -> dict:
        """Convierte Appointment a dict con strings para Redis"""
        # Obtener el dict del modelo
        data = appointment.model_dump()
        
        # Convertir todo a string
        data['date'] = appointment.date.isoformat() if hasattr(appointment.date, 'isoformat') else str(appointment.date)
        data['time'] = appointment.time.isoformat() if hasattr(appointment.time, 'isoformat') else str(appointment.time)
        data['createdAt'] = appointment.createdAt.isoformat()
        data['updatedAt'] = appointment.updatedAt.isoformat()
        data['patient'] = json.dumps(appointment.patient.model_dump())
        
        return data

    async def save(self, appointment: Appointment) -> str:
        """Guarda una cita en Redis"""
        # Generar ID único
        appointment_id = await self.redis_client.incr("appointment:next_id")
        appointment.id = str(appointment_id)
        
        # Guardar en Hash
        key = f"appointment:{appointment_id}"
        await self.redis_client.hset(key, mapping=self._to_redis_dict(appointment))
        
        # Índice por fecha (para búsquedas rápidas)
        date_ts = int(datetime.fromisoformat(appointment.date.isoformat()).timestamp())
        await self.redis_client.zadd("appointments_by_date", {str(appointment_id): date_ts})
        
        # Índice único por fecha+hora (para evitar duplicados)
        unique_key = f"slot:{appointment.date.isoformat()}:{appointment.time.isoformat()}"
        await self.redis_client.set(unique_key, str(appointment_id))
        
        return str(appointment_id)

    async def exists_by_date_and_time(self, date_str: str, time_str: str) -> bool:
        """Verifica si ya existe una cita en esa fecha y hora (usando índice único)"""
        unique_key = f"slot:{date_str}:{time_str}"
        return await self.redis_client.exists(unique_key) > 0

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
            appt = await self.find_by_id(aid)
            if appt:
                appointments.append(appt)
        return appointments

    async def update_state(self, appointment_id: str, state: str) -> bool:
        key = f"appointment:{appointment_id}"
        exists = await self.redis_client.exists(key)
        if not exists:
            return False
        await self.redis_client.hset(key, mapping={"state": state, "updatedAt": datetime.now().isoformat()})
        return True

    async def delete(self, appointment_id: str) -> bool:
        # Obtener la cita para limpiar índices
        appt = await self.find_by_id(appointment_id)
        if appt:
            unique_key = f"slot:{appt['date']}:{appt['time']}"
            await self.redis_client.delete(unique_key)
        
        key = f"appointment:{appointment_id}"
        deleted = await self.redis_client.delete(key)
        return deleted > 0

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[dict]:
        keys = await self.redis_client.keys("appointment:*")
        keys = [k for k in keys if k != "appointment:next_id"]
        
        keys = keys[skip:skip + limit]
        
        appointments = []
        for key in keys:
            appt = await self.find_by_id(key.split(":")[1])
            if appt:
                appointments.append(appt)
        return appointments