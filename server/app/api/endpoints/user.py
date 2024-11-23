from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.patient import Patient
from app.models.doctor import Doctor
from app.schemas.patient import PatientCreate, PatientRead
from app.schemas.doctor import DoctorCreate, DoctorRead

router = APIRouter()

# Endpoint untuk membuat pasien baru
@router.post("/patients/", response_model=PatientRead)
async def create_patient(patient: PatientCreate, db: AsyncSession = Depends(get_db)):
    db_patient = Patient(**patient.dict())
    db.add(db_patient)
    await db.commit()
    await db.refresh(db_patient)
    return db_patient

# Endpoint untuk mendapatkan data pasien berdasarkan ID
@router.get("/patients/{patient_id}", response_model=PatientRead)
async def read_patient(patient_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Patient).where(Patient.id == patient_id))
    patient = result.scalars().first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

# Endpoint untuk membuat dokter baru
@router.post("/doctors/", response_model=DoctorRead)
async def create_doctor(doctor: DoctorCreate, db: AsyncSession = Depends(get_db)):
    db_doctor = Doctor(**doctor.dict())
    db.add(db_doctor)
    await db.commit()
    await db.refresh(db_doctor)
    return db_doctor

# Endpoint untuk mendapatkan data dokter berdasarkan ID
@router.get("/doctors/{doctor_id}", response_model=DoctorRead)
async def read_doctor(doctor_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Doctor).where(Doctor.id == doctor_id))
    doctor = result.scalars().first()
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor
