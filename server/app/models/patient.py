from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.models.base import Base

class Patient(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    gender = Column(String)

    appointments = relationship("Appointment", back_populates="patient")
    analysis_results = relationship("AnalysisResult", back_populates="patient")
    medical_images = relationship("MedicalImage", back_populates="patient")
