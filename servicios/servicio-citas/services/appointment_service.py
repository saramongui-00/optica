from repositories.appointment_repository import AppointmentRepository
from models.appointment import Appointment
from models.enums import AppointmentState

citas_temporales = []

class AppointmentService:
    def __init__(self):
        self.repository = AppointmentRepository()

    def _serialize_appointment(self, appointment_dict: dict) -> dict:
        if appointment_dict and "_id" in appointment_dict:
            appointment_dict["id"] = str(appointment_dict["_id"])
            del appointment_dict["_id"]
        return appointment_dict

    async def create_appointment(self, appointment_data: dict) -> dict:
        global citas_temporales
        
        fecha = appointment_data["date"]
        hora = appointment_data["time"]
        
        for cita in citas_temporales:
            if cita.get("date") == fecha and cita.get("time") == hora:
                raise Exception(f"Ya existe una cita para {fecha} a las {hora}")
        
        appointment = Appointment(**appointment_data)
        appointment_id = await self.repository.save(appointment)
        
        appointment_dict = appointment.model_dump()
        appointment_dict["id"] = appointment_id
        citas_temporales.append(appointment_dict)
        
        return {"id": appointment_id, "message": "Cita creada exitosamente"}

    async def cancel_appointment(self, appointment_id: str) -> dict:
        updated = await self.repository.update_state(appointment_id, AppointmentState.CANCELLED.value)
        if not updated:
            raise Exception("Appointment not found")
        return {"message": "Appointment cancelled successfully"}

    async def modify_appointment(self, appointment_id: str, data: dict) -> dict:
        updated = await self.repository.update(appointment_id, data)
        if not updated:
            raise Exception("Appointment not found")
        return {"message": "Appointment modified successfully"}

    async def get_appointment_by_id(self, appointment_id: str) -> dict:
        appointment = await self.repository.find_by_id(appointment_id)
        if not appointment:
            raise Exception("Appointment not found")
        return self._serialize_appointment(appointment)

    async def get_appointments_by_date(self, date: str) -> dict:
        appointments = await self.repository.find_by_date(date)
        return {
            "date": date,
            "total": len(appointments),
            "appointments": [self._serialize_appointment(a) for a in appointments]
        }

    async def get_appointments_by_patient(self, document: str) -> dict:
        appointments = await self.repository.find_by_patient_document(document)
        return {
            "patientDocument": document,
            "total": len(appointments),
            "appointments": [self._serialize_appointment(a) for a in appointments]
        }

    async def get_all_appointments(self, page: int = 1, limit: int = 10) -> dict:
        global citas_temporales
        start = (page - 1) * limit
        end = start + limit
        
        return {
            "page": page,
            "limit": limit,
            "total": len(citas_temporales),
            "appointments": citas_temporales[start:end]
        }