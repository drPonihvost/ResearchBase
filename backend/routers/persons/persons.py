from fastapi import APIRouter
from fastapi.params import Depends

from sqlalchemy.orm import Session

from backend.routers.research.schemas import ResearchSchema
from backend.routers.research.models import Research


router = APIRouter()

tag = ['Persons']


@router.get('/', tags=tag)
async def get_all_persons():
    return {'researches': ['routers']}