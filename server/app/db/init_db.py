from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import engine
from app.models import base
from app.models import patient, doctor, appointment, analysisresult, medicalimage

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(base.Base.metadata.create_all)
