from pydantic import BaseModel

class Acudiente(BaseModel):
    nombre: str
    telefono: str
    parentesco: str
    correo: str | None = None
    