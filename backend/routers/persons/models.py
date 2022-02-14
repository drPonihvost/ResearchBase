from sqlalchemy import Column, String, Date, Boolean, Integer, ForeignKey

from backend.core.models.database import DataBaseModel
from backend.routers.research.models import Research
from sqlalchemy.orm import relationship


class Person(DataBaseModel):
    __tablename__ = 'person'
    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    male = Column(Boolean)
    birthday = Column(Date)
    birthplace = Column(String)
    relation = Column(String)
    research_id = Column(Integer, ForeignKey('research.id'))

    research = relationship('Research', backref='person')


