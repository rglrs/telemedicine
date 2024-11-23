from pydantic import BaseModel
from datetime import datetime

class AppointmentBase(BaseModel):
    appointment_date: datetime
    reason: str

class AppointmentCreate(AppointmentBase):
    patient_id: int
    doctor_id: int

class AppointmentRead(AppointmentBase):
    id: int

    class Config:
        from_attributes = True
