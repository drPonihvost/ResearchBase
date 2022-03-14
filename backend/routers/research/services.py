import os
from typing import List

from sqlalchemy.orm import Session
from backend.routers.research.models import Research
from backend.routers.research.schemas import ResearchSchemaCreate


def get_all_research(db: Session):
    return db.query(Research).all()


def get_research_by_id(db: Session, research_id):
    return db.query(Research).get(research_id)


def create_research(db: Session, item: ResearchSchemaCreate):
    research = Research(**item.dict())
    db.add(research)
    db.commit()
    db.refresh(research)
    return research


def create_file(db: Session, research_list: List[int]):
    file_string = ''
    for research_id in research_list:
        research = db.query(Research).get(research_id)
        file_string += f'{research.id}\t{research.event_number}\t{research.incident_date}\n'
    with open('text.txt', 'w') as file:
        file.write(file_string)
        path = r'C:\Users\kudro\Desktop\FastAPI\ResearchBase\backend\text.txt'
        return path
