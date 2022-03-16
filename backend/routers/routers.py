from fastapi import APIRouter

from backend.routers.research import research

routers = APIRouter()
routers.include_router(research.router, prefix='/research')

