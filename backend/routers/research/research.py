from fastapi import APIRouter
from core.schemas.schema import Research

router = APIRouter()


@router.get('/researches')
async def research():
    return {'researches': ['routers']}


@router.post('/researches')
async def create_research(research: Research):
    return research


@router.get('/researches/{research_id}')
async def research(research_id: int):
    return {'researches': research_id}