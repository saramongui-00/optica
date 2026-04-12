from pydantic import BaseModel, Field, computed_field
from datetime import date
from typing import Optional
from models.enums import Sexo, EstadoCivil
from models.acudiente import Acudiente

class Paciente(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    documento: str
    nombres: str
    apellidos: str
    sexo: Sexo
    fecha_nacimiento: str
    estado_civil: EstadoCivil
    ocupacion: str
    departamento: str
    ciudad: str
    direccion: str
    correo_electronico: str
    telefono: str
    eps: str
    fecha_admision: str = Field(default_factory=lambda: date.today().isoformat())  # ← Cambiado
    acudiente: Optional[Acudiente] = None
    
    @computed_field
    @property
    def edad(self) -> int:
        if isinstance(self.fecha_nacimiento, str):
            nacimiento = date.fromisoformat(self.fecha_nacimiento)
        else:
            nacimiento = self.fecha_nacimiento
        today = date.today()
        return today.year - nacimiento.year - (
            (today.month, today.day) < (nacimiento.month, nacimiento.day)
        )
    
    class Config:
        populate_by_name = True