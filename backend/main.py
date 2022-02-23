import uvicorn
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import Response

from backend.routers.routers import routers
from backend.core.models.database import SessionLocal, init_db
from backend.core.settings import settings


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


@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internal server error', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


app.include_router(routers)


if __name__ == '__main__':
    init_db()
    uvicorn.run('main:app', reload=True)
