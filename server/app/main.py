from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import patient, doctor, appointment, analysisresult, schedule, medicalimage, user
from app.db.init_db import init_db

app = FastAPI()

# Konfigurasi CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ubah dengan daftar domain yang diizinkan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient.router, prefix="/patients", tags=["patients"])
app.include_router(doctor.router, prefix="/doctors", tags=["doctors"])
app.include_router(appointment.router, prefix="/appointments", tags=["appointments"])
app.include_router(analysisresult.router, prefix="/analysisresults", tags=["analysisresults"])
app.include_router(schedule.router, prefix="/schedules", tags=["schedules"])
app.include_router(medicalimage.router, prefix="/medicalimages", tags=["medicalimages"])
app.include_router(user.router, prefix="/users", tags=["users"])

# @app.on_event("startup")
# async def on_startup():
#     await init_db()
