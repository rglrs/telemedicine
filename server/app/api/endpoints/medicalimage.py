from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.medicalimage import MedicalImage
from app.schemas.medicalimage import MedicalImageCreate, MedicalImageRead
from datetime import datetime
import shutil
import os

router = APIRouter()

UPLOAD_DIRECTORY = "uploads/"

# Endpoint untuk mengunggah gambar medis
@router.post("/", response_model=MedicalImageRead)
async def upload_medical_image(patient_id: int, image_type: str, file: UploadFile = File(...), db: AsyncSession = Depends(get_db)):
    if not os.path.exists(UPLOAD_DIRECTORY):
        os.makedirs(UPLOAD_DIRECTORY)
    
    file_path = os.path.join(UPLOAD_DIRECTORY, file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    db_medical_image = MedicalImage(
        upload_date=datetime.utcnow(),
        image_type=image_type,
        image_url=file_path,
        patient_id=patient_id
    )
    db.add(db_medical_image)
    await db.commit()
    await db.refresh(db_medical_image)
    return db_medical_image

# Endpoint untuk mendapatkan data gambar medis berdasarkan ID
@router.get("/{medical_image_id}", response_model=MedicalImageRead)
async def read_medical_image(medical_image_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(MedicalImage).where(MedicalImage.id == medical_image_id))
    medical_image = result.scalars().first()
    if not medical_image:
        raise HTTPException(status_code=404, detail="MedicalImage not found")
    return medical_image
