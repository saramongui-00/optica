from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, Field, computed_field
from models.enums import Sexo, EstadoCivil
from models.acudiente import Acudiente

class Paciente(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    documento: str
    nombres: str
    apellidos: str
    sexo: Sexo
    fecha_nacimiento: date
    estado_civil: EstadoCivil
    ocupacion: str
    departamento: str
    ciudad: str
    direccion: str
    correo_electronico: str
    telefono: str
    eps: str
    fecha_admision: date = Field(default_factory=date.today)
    acudiente: Optional[Acudiente] = None
    
    @computed_field
    @property
    def edad(self) -> int:
        today = date.today()
        return today.year - self.fecha_nacimiento.year - (
            (today.month, today.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )
    
    class Config:
        populate_by_name = True