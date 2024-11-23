from pydantic import BaseModel

class DoctorBase(BaseModel):
    name: str
    specialty: str
    email: str

class DoctorCreate(DoctorBase):
    password: str

class DoctorRead(DoctorBase):
    id: int

    class Config:
        from_attributes = True
