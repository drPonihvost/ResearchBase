from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from backend.core.database import DataBase


class BaseModel(DataBase):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)


class Research(BaseModel):
    __tablename__ = 'researches'

    reg_number = Column(Integer)
    date_of_record = Column(Date)
    initiator_department = Column(String)
    initiator_post = Column(String)
    initiator_rank = Column(String)
    initiator_surname = Column(String)
    initiator_name = Column(String)
    initiator_patronymic = Column(String)
    executor_department = Column(String)
    executor_post = Column(String)
    executor_rank = Column(String)
    executor_surname = Column(String)
    executor_name = Column(String)
    executor_patronymic = Column(String)
    event_number = Column(String)
    formation_date = Column(Date)
    article = Column(String)
    plot = Column(String)
    incident_date = Column(Date)
    address = Column(String)
    relative_search = Column(Boolean, default=False)
    reg_date = Column(Date)

    persons = relationship('Person', back_populates='researches')


class Person(BaseModel):
    __tablename__ = 'persons'

    surname = Column(String)
    name = Column(String)
    patronymic = Column(String)
    male = Column(Boolean)
    birthday = Column(Date)
    birthplace = Column(String)
    relation = Column(String)
    research_id = Column(Integer, ForeignKey('researches.id'))

    researches = relationship('Research', back_populates='persons')
