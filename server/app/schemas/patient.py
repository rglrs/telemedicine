from pydantic import BaseModel
from datetime import date

class PatientBase(BaseModel):
    name: str
    email: str
    gender: str

class PatientCreate(PatientBase):
    password: str

class PatientRead(PatientBase):
    id: int

    class Config:
        from_attributes = True
