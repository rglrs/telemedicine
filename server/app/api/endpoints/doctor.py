from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorRead

router = APIRouter()

@router.post("/", response_model=DoctorRead)
async def create_doctor(doctor: DoctorCreate, db: AsyncSession = Depends(get_db)):
    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    await db.commit()
    await db.refresh(db_doctor)
    return db_doctor

@router.get("/{doctor_id}", response_model=DoctorRead)
async def read_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Doctor).where(Doctor.id == doctor_id))
    doctor = result.scalars().first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
