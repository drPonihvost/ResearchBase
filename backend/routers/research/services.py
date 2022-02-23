from sqlalchemy.orm import Session
from backend.routers.research.models import Research
from backend.routers.research.schemas import ResearchSchemaCreate


def get_all_research(db: Session):
    return db.query(Research).all()


def create_research(db: Session, item: ResearchSchemaCreate):
    print(item.dict())
    research = Research(**item.dict())
    db.add(research)
    db.commit()
    db.refresh(research)
    return research
