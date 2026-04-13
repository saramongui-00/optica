from repositories.appointment_repository import AppointmentRepository
from models.appointment import Appointment
from models.enums import AppointmentState

class AppointmentService:
    def __init__(self):
        self.repository = AppointmentRepository()

    async def create_appointment(self, appointment_data: dict) -> dict:
        """Crear una nueva cita con validación atómica"""
        fecha = appointment_data["date"]
        hora = appointment_data["time"]
        
        # Validación usando índice único
        existe = await self.repository.exists_by_date_and_time(fecha, hora)
        if existe:
            raise Exception(f"Ya existe una cita para {fecha} a las {hora}")
        
        # Crear y guardar
        appointment = Appointment(**appointment_data)
        appointment_id = await self.repository.save(appointment)
        
        return {"id": appointment_id, "message": "Cita creada exitosamente"}

    async def cancel_appointment(self, appointment_id: str) -> dict:
        updated = await self.repository.update_state(appointment_id, AppointmentState.CANCELLED.value)
        if not updated:
            raise Exception("Cita no encontrada")
        return {"message": "Cita cancelada exitosamente"}

    async def get_appointment_by_id(self, appointment_id: str) -> dict:
        appointment = await self.repository.find_by_id(appointment_id)
        if not appointment:
            raise Exception("Cita no encontrada")
        return appointment

    async def get_appointments_by_date(self, date: str) -> dict:
        appointments = await self.repository.find_by_date(date)
        return {
            "date": date,
            "total": len(appointments),
            "appointments": appointments
        }

    async def get_all_appointments(self, page: int = 1, limit: int = 10) -> dict:
        skip = (page - 1) * limit
        appointments = await self.repository.get_all(skip, limit)
        
        return {
            "page": page,
            "limit": limit,
            "total": len(appointments),
            "appointments": appointments
        }