from fastapi import APIRouter

from backend.routers.research import research
from backend.routers.persons import persons

routers = APIRouter()
routers.include_router(research.router, prefix='/research')
routers.include_router(persons.router, prefix='/persons')

