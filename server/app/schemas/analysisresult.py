from pydantic import BaseModel
from datetime import datetime

class AnalysisResultBase(BaseModel):
    analysis_date: datetime
    result_type: str
    result_value: str

class AnalysisResultCreate(AnalysisResultBase):
    patient_id: int

class AnalysisResultRead(AnalysisResultBase):
    id: int

    class Config:
        from_attributes = True
