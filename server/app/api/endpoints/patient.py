from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.patient import Patient
from app.schemas.patient import PatientCreate, PatientRead
from typing import List

router = APIRouter()

@router.post("/", response_model=PatientRead)
async def create_patient(patient: PatientCreate, db: AsyncSession = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    await db.commit()
    await db.refresh(db_patient)
    return db_patient

@router.get("/{patient_id}", response_model=PatientRead)
async def read_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Patient).where(Patient.id == patient_id))
    patient = result.scalars().first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.get("/", response_model=List[PatientRead])
async def read_all_patients(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Patient).offset(skip).limit(limit))
    patients = result.scalars().all()
    return patients
