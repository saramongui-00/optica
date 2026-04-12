from fastapi import APIRouter, HTTPException, Query
from services.appointment_service import AppointmentService
from models.appointment import Appointment
from models.enums import AppointmentState

router = APIRouter(prefix="/api/appointments", tags=["Appointments"])
service = AppointmentService()

@router.post("/")
async def create_appointment(appointment: Appointment):
    try:
        result = await service.create_appointment(appointment.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.put("/{appointment_id}/cancel")
async def cancel_appointment(appointment_id: str):
    try:
        return await service.cancel_appointment(appointment_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{appointment_id}")
async def modify_appointment(appointment_id: str, data: dict):
    try:
        return await service.modify_appointment(appointment_id, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{appointment_id}")
async def get_appointment_by_id(appointment_id: str):
    try:
        return await service.get_appointment_by_id(appointment_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/date/{date}")
async def get_appointments_by_date(date: str):
    try:
        return await service.get_appointments_by_date(date)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/patient/{document}")
async def get_appointments_by_patient(document: str):
    try:
        return await service.get_appointments_by_patient(document)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/")
async def get_all_appointments(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=50)):
    return await service.get_all_appointments(page, limit)

@router.get("/enums/states")
async def get_appointment_states():
    return [{"value": s.value, "label": s.name} for s in AppointmentState]