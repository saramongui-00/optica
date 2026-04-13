from fastapi import APIRouter, HTTPException, Query
from services.patient_service import PatientService
from models.patient import Paciente
from models.enums import Sexo, EstadoCivil

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])
service = PatientService()

@router.post("/")
async def create_patient(paciente: Paciente):
    try:
        result = await service.create_patient(paciente.model_dump())
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{patient_id}")
async def get_patient(patient_id: str):
    try:
        return await service.get_patient(patient_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/documento/{documento}")
async def get_patient_by_documento(documento: str):
    try:
        return await service.get_patient_by_documento(documento)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.put("/{patient_id}")
async def update_patient(patient_id: str, data: dict):
    try:
        return await service.update_patient(patient_id, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{patient_id}")
async def delete_patient(patient_id: str):
    try:
        return await service.delete_patient(patient_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/")
async def get_all_patients(page: int = Query(1, ge=1), limit: int = Query(10, ge=1, le=50)):
    return await service.get_all_patients(page, limit)

@router.get("/enums/sexo")
async def get_sexos():
    return [{"value": e.value, "label": e.name} for e in Sexo]

@router.get("/enums/estado-civil")
async def get_estados_civiles():
    return [{"value": e.value, "label": e.name} for e in EstadoCivil]