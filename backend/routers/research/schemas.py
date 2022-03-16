from typing import Optional

from pydantic import BaseModel
import datetime


class ResearchBase(BaseModel):
    reg_number: int
    date_of_record: datetime.date
    initiator_department: str
    initiator_post: str
    initiator_rank: str
    initiator_surname: str
    initiator_name: str
    initiator_patronymic: str
    executor_department: str
    executor_post: str
    executor_rank: str
    executor_surname: str
    executor_name: str
    executor_patronymic: str
    event_number: str
    formation_date: datetime.date
    article: str
    plot: str
    incident_date: datetime.date
    address: str
    relative_search: bool
    reg_date: Optional[datetime.date] = None


class ResearchCreate(ResearchBase):
    pass


class Research(ResearchBase):
    id: int

    class Config:
        orm_mode = True


class PersonBase(BaseModel):
    surname: str
    name: str
    patronymic: str
    birthday: datetime.date
    birthplace: str
    relation: Optional[str] = ''


class PersonCreate(PersonBase):
    pass


class Person(PersonBase):
    id: int

    class Config:
        orm_mode = True
