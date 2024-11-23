from pydantic import BaseModel
from datetime import datetime

class MedicalImageBase(BaseModel):
    upload_date: datetime
    image_type: str
    image_url: str

class MedicalImageCreate(MedicalImageBase):
    patient_id: int

class MedicalImageRead(MedicalImageBase):
    id: int

    class Config:
        from_attributes = True
