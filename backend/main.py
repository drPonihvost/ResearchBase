import uvicorn
from fastapi import FastAPI
from routers.research import research
from backend.routers.research.models import *
from backend.routers.persons.models import *
from core.models.database import init_db
from core.settings import settings


app = FastAPI(
    title=settings.TITLE,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    contact={
        'name': settings.NAME,
        'email': settings.EMAIL
    },
    openapi_tags=settings.TAGS_METADATA
)
app.include_router(research.router)


if __name__ == '__main__':
    init_db()
    uvicorn.run('main:app', reload=True)
