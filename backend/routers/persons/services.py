from sqlalchemy.orm import Session
from backend.routers.persons.models import Person


def get_person_count(db: Session, research_id):
    return db.query(Person).filter_by(research_id=research_id)
