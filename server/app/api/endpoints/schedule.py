from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from app.db.session import get_db
from app.models.appointment import Appointment
from app.schemas.appointment import AppointmentCreate, AppointmentRead

router = APIRouter()

@router.post("/", response_model=AppointmentRead)
async def create_appointment(appointment: AppointmentCreate, db: AsyncSession = Depends(get_db)):
    db_appointment = Appointment(**appointment.dict())
    db.add(db_appointment)
    await db.commit()
    await db.refresh(db_appointment)
    return db_appointment

@router.get("/", response_model=List[AppointmentRead])
async def read_appointments(skip: int = 0, limit: int = 10, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Appointment).offset(skip).limit(limit))
    return result.scalars().all()

@router.get("/{appointment_id}", response_model=AppointmentRead)
async def read_appointment(appointment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Appointment).where(Appointment.id == appointment_id))
    appointment = result.scalars().first()
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment
