from fastapi import APIRouter, Query, Request
from fastapi.params import Depends
from fastapi.staticfiles import StaticFiles
from starlette.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from backend.core.utils import get_db
from backend.routers.research.services import *
from backend.routers.research.schemas import ResearchSchemaCreate, ResearchSchemaList

router = APIRouter()

tag = ['Research']

templates = Jinja2Templates(directory='routers/research/templates')


@router.get('/dep', tags=tag, response_class=HTMLResponse)
async def research(request: Request, db: Session = Depends(get_db)):
    data = get_all_research(db)
    return templates.TemplateResponse('research.html', {"request": request, "data": data})


# @router.get('/', tags=tag, response_model=List[ResearchSchemaList])
# async def researches(db: Session = Depends(get_db)):
#     return get_all_research(db)
#
#
@router.post('/', tags=tag)
async def research(item: ResearchSchemaCreate, db: Session = Depends(get_db)):
    return create_research(db, item)


@router.delete('/{id}', tags=tag)
async def research(id: int, db: Session = Depends(get_db)):
    return delete_research(db, id)
#
#
# @router.get('/{research_id}', tags=tag, response_model=ResearchSchemaList)
# async def researches(research_id: int, db: Session = Depends(get_db)):
#     return get_research_by_id(db, research_id)
#
#
# @router.get('/import/', tags=tag)
# async def get_researches(research_list: List[int] = Query(None), db: Session = Depends(get_db)):
#     return FileResponse(create_file(db, research_list), media_type='application/octet-stream', filename='import.txt')
