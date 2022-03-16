from typing import List

from sqlalchemy.orm import Session
from backend.routers.research import models
from backend.routers.research import schemas


def get_all_research(db: Session):
    return db.query(models.Research).all()


def get_research_by_id(db: Session, research_id):
    return db.query(models.Research).get(research_id)


def delete_research(db: Session, research_id):
    db.delete(get_research_by_id(db, research_id))
    db.commit()


def create_research(db: Session, item: schemas.ResearchCreate):
    research = models.Research(**item.dict())
    db.add(research)
    db.commit()
    db.refresh(research)
    return research


def create_file(db: Session, research_list: List[int]):
    file_string = ''
    for research_id in research_list:
        research = db.query(models.Research).get(research_id)
        file_string += f'{research.id}\t{research.event_number}\t{research.incident_date}\n'
    with open('text.txt', 'w') as file:
        file.write(file_string)
        path = r'C:\Users\kudro\Desktop\FastAPI\ResearchBase\backend\text.txt'
        return path


def get_persons_by_research(db: Session, research_id):
    return db.query(models.Person).filter(models.Person.research_id == research_id).all()


def create_person(db: Session, research_id, item: schemas.PersonCreate):
    person = models.Person(**item.dict(), research_id=research_id)
    db.add(person)
    db.commit()
    db.refresh(person)
    return person
