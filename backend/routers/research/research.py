from fastapi import APIRouter, Query, Request, HTTPException
from fastapi.params import Depends
from starlette.responses import FileResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List

from backend.core.database import engine
from backend.core.utils import get_db
from backend.routers.research.services import *
from backend.routers.research import schemas

router = APIRouter()

tag = ['Research']

templates = Jinja2Templates(directory='templates/research')


@router.get('/', tags=tag, response_model=List[schemas.Research])
async def researches(db: Session = Depends(get_db)):
    return get_all_research(db)


@router.get('/dep', tags=tag, response_class=HTMLResponse)
async def research(request: Request, db: Session = Depends(get_db)):
    data = get_all_research(db)
    return templates.TemplateResponse('research.html', {'request': request, 'data': data})


@router.get('/{research_id}/persons', tags=tag, response_model=List[schemas.Person])
async def get_persons(research_id: int, db: Session = Depends(get_db)):
    research_ = get_research_by_id(db, research_id)
    if research_ is None:
        raise HTTPException(status_code=404, detail='Research not found')
    return get_persons_by_research(db, research_id)


@router.post('/{research_id}/persons', tags=tag, response_model=schemas.Person)
async def add_person(research_id: int, item: schemas.PersonCreate, db: Session = Depends(get_db)):
    research_ = get_research_by_id(db, research_id)
    if research_ is None:
        raise HTTPException(status_code=404, detail='Research not found')
    return create_person(db, research_id, item)

# @router.get('/', tags=tag, response_model=List[ResearchSchemaList])
# async def researches(db: Session = Depends(get_db)):
#     return get_all_research(db)


@router.post('/', tags=tag)
async def research(item: schemas.ResearchCreate, db: Session = Depends(get_db)):
    return create_research(db, item)


@router.delete('/{id}', tags=tag)
async def research(research_id: int, db: Session = Depends(get_db)):
    return delete_research(db, research_id)


# @router.get('/{research_id}', tags=tag, response_model=ResearchSchemaList)
# async def researches(research_id: int, db: Session = Depends(get_db)):
#     return get_research_by_id(db, research_id)


@router.get('/import', tags=tag)
async def get_researches(research_list: List[int] = Query(None), db: Session = Depends(get_db)):
    return FileResponse(create_file(db, research_list), media_type='application/octet-stream', filename='import.txt')
