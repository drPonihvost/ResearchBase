from pydantic import BaseModel
from datetime import datetime


class ResearchSchema(BaseModel):
    reg_number: int
    reg_date: str
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
    formation_date: str
    article: str
    plot: str
    incident_date: str
    address: str

    class Config:
        orm_mode = True


class ResearchSchemaList(ResearchSchema):
    id: int


class ResearchSchemaCreate(ResearchSchema):
    pass
