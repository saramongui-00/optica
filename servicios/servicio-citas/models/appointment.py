from datetime import datetime, date, time
from typing import Optional
from pydantic import BaseModel, Field
from models.enums import AppointmentState
from models.patient import Patient

class Appointment(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    date: date
    time: time
    patient: Patient
    state: AppointmentState = AppointmentState.AGENDADA
    createdAt: datetime = Field(default_factory=datetime.now)
    updatedAt: datetime = Field(default_factory=datetime.now)
    
    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "date": "2025-05-15",
                "time": "10:30:00",
                "patient": {
                    "document": "12345678",
                    "firstName": "Ana",
                    "lastName": "Gómez",
                    "phone": "3001234567",
                    "email": "ana@example.com"
                }
            }
        }