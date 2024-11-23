from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class MedicalImage(Base):
    id = Column(Integer, primary_key=True, index=True)
    upload_date = Column(DateTime)
    image_type = Column(String)  # X-ray atau CT scan
    image_url = Column(String)  # URL atau path ke file gambar
    patient_id = Column(Integer, ForeignKey('patient.id'))

    patient = relationship("Patient", back_populates="medical_images")
