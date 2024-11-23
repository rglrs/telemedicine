from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class Appointment(Base):
    id = Column(Integer, primary_key=True, index=True)
    appointment_date = Column(DateTime)
    reason = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))
    doctor_id = Column(Integer, ForeignKey('doctor.id'))

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
