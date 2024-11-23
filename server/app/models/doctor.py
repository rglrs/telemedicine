from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models.base import Base

class Doctor(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialty = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    appointments = relationship("Appointment", back_populates="doctor")
