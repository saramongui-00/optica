from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):
    id: Optional[str] = None
    document: str
    firstName: str
    lastName: str
    phone: str
    email: str