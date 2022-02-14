from fastapi import APIRouter
from fastapi.params import Depends

from sqlalchemy.orm import Session

from backend.routers.research.schemas import ResearchSchema
from backend.routers.research.models import Research

from backend.core.models.database import get_db

router = APIRouter()

tag = ['Research']


@router.get('/researches', tags=tag)
async def research():
    return {'researches': ['routers']}


@router.post('/researches', tags=tag)
async def create_research(research_data: ResearchSchema, db: Session = Depends(get_db)):
    research = Research(**research_data.dict())
    db.add(research)
    db.commit()
    db.refresh(research)
    return research


@router.get('/researches/{research_id}', tags=tag)
async def research(research_id: int):
    return {'researches': research_id}
