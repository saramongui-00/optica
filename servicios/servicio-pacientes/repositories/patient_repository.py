from pymongo import AsyncMongoClient
from models.patient import Paciente
from bson import ObjectId
import os

class PatientRepository:
    def __init__(self):
        self.client = AsyncMongoClient(os.getenv("MONGO_URL", "mongodb://localhost:27017"))
        self.db = self.client.optica_db
        self.collection = self.db.pacientes

    def _to_dict(self, paciente: Paciente) -> dict:
        data = paciente.model_dump(by_alias=True, exclude={"id"})
        
        # Convertir fechas a string solo si son objetos date
        if 'fecha_nacimiento' in data and data['fecha_nacimiento']:
            if hasattr(data['fecha_nacimiento'], 'isoformat'):
                data['fecha_nacimiento'] = data['fecha_nacimiento'].isoformat()
        
        if 'fecha_admision' in data and data['fecha_admision']:
            if hasattr(data['fecha_admision'], 'isoformat'):
                data['fecha_admision'] = data['fecha_admision'].isoformat()
        
        return data

    async def save(self, paciente: Paciente) -> str:
        result = await self.collection.insert_one(self._to_dict(paciente))
        return str(result.inserted_id)

    async def find_by_id(self, patient_id: str) -> dict | None:
        return await self.collection.find_one({"_id": ObjectId(patient_id)})

    async def find_by_documento(self, documento: str) -> dict | None:
        return await self.collection.find_one({"documento": documento})

    async def find_by_email(self, email: str) -> dict | None:
        return await self.collection.find_one({"correo_electronico": email})

    async def update(self, patient_id: str, data: dict) -> bool:
        result = await self.collection.update_one(
            {"_id": ObjectId(patient_id)}, 
            {"$set": data}
        )
        return result.modified_count > 0

    async def delete(self, patient_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(patient_id)})
        return result.deleted_count > 0

    async def get_all(self, skip: int = 0, limit: int = 100) -> list:
        cursor = self.collection.find().skip(skip).limit(limit)
        return await cursor.to_list(length=limit)