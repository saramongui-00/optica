from repositories.patient_repository import PatientRepository
from models.patient import Paciente
import json

class PatientService:
    def __init__(self):
        self.repository = PatientRepository()

    def _serialize_paciente(self, paciente_dict: dict) -> dict:
        if paciente_dict and "_id" in paciente_dict:
            paciente_dict["id"] = str(paciente_dict["_id"])
            del paciente_dict["_id"]
        return paciente_dict

    async def create_patient(self, patient_data: dict) -> dict:
        existente = await self.repository.find_by_documento(patient_data["documento"])
        if existente:
            raise Exception("Ya existe un paciente con este documento")
        
        existente_email = await self.repository.find_by_email(patient_data["correo_electronico"])
        if existente_email:
            raise Exception("Ya existe un paciente con este correo")
        
        paciente = Paciente(**patient_data)
        patient_id = await self.repository.save(paciente)
        
        return {"id": patient_id, "message": "Paciente creado exitosamente"}

    async def get_patient(self, patient_id: str) -> dict:
        paciente = await self.repository.find_by_id(patient_id)
        if not paciente:
            raise Exception("Paciente no encontrado")
        return self._serialize_paciente(paciente)

    async def get_patient_by_documento(self, documento: str) -> dict:
        paciente = await self.repository.find_by_documento(documento)
        if not paciente:
            raise Exception("Paciente no encontrado")
        return self._serialize_paciente(paciente)

    async def update_patient(self, patient_id: str, data: dict) -> dict:
        updated = await self.repository.update(patient_id, data)
        if not updated:
            raise Exception("Paciente no encontrado")
        return {"message": "Paciente actualizado"}

    async def delete_patient(self, patient_id: str) -> dict:
        deleted = await self.repository.delete(patient_id)
        if not deleted:
            raise Exception("Paciente no encontrado")
        return {"message": "Paciente eliminado"}

    async def get_all_patients(self, page: int = 1, limit: int = 10) -> dict:
        skip = (page - 1) * limit
        pacientes = await self.repository.get_all(skip, limit)
        
        return {
            "page": page,
            "limit": limit,
            "total": len(pacientes),
            "data": [self._serialize_paciente(p) for p in pacientes]
        }