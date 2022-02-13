from pydantic import BaseModel
from datetime import date


class Research(BaseModel):
    id: int
    date: date
    initiator_surname: str
    initiator_name: str
    initiator_patronymic: str
    executor_surname: str
    executor_name: str
    executor_patronymic: str
    number: str
    formation_date: str
    article: str
    plot: str
    incident_date: str
    address: str


class Person(BaseModel):
    surname: str
    name: str
    patronymic: str
    birthday: date
    birthplace: str
    relation: str = None




