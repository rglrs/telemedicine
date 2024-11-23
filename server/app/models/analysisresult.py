from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.models.base import Base

class AnalysisResult(Base):
    id = Column(Integer, primary_key=True, index=True)
    analysis_date = Column(DateTime)
    result_type = Column(String)
    result_value = Column(String)
    patient_id = Column(Integer, ForeignKey('patient.id'))

    patient = relationship("Patient", back_populates="analysis_results")
