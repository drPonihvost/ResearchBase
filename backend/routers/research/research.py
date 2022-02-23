from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session
from typing import List

from backend.core.utils import get_db
from backend.routers.research.services import *
from backend.routers.research.schemas import ResearchSchemaCreate, ResearchSchemaList

router = APIRouter()

tag = ['Research']


@router.get('/', tags=tag, response_model=List[ResearchSchemaList])
async def researches(db: Session = Depends(get_db)):
    return get_all_research(db)


@router.post('/', tags=tag)
async def researches(item: ResearchSchemaCreate, db: Session = Depends(get_db)):
    return create_research(db, item)


# @router.get('/{research_id}', tags=tag)
# async def research(research_id: int):
#     return {'researches': research_id}
