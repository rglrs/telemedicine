from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.session import get_db
from app.models.analysisresult import AnalysisResult
from app.schemas.analysisresult import AnalysisResultCreate, AnalysisResultRead

router = APIRouter()

@router.post("/", response_model=AnalysisResultRead)
async def create_analysis_result(analysis_result: AnalysisResultCreate, db: AsyncSession = Depends(get_db)):
    db_analysis_result = AnalysisResult(**analysis_result.dict())
    db.add(db_analysis_result)
    await db.commit()
    await db.refresh(db_analysis_result)
    return db_analysis_result

@router.get("/{analysis_result_id}", response_model=AnalysisResultRead)
async def read_analysis_result(analysis_result_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(AnalysisResult).where(AnalysisResult.id == analysis_result_id))
    analysis_result = result.scalars().first()
    if not analysis_result:
        raise HTTPException(status_code=404, detail="AnalysisResult not found")
    return analysis_result
