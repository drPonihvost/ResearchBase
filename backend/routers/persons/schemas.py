from pydantic import BaseModel
from datetime import date


class Person(BaseModel):
    surname: str
    name: str
    patronymic: str
    birthday: date
    birthplace: str
    relation: str = ''
