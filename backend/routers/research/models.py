from sqlalchemy import Column, Integer, String, DateTime
from backend.core.models.database import DataBase


class Research(DataBase):
    __tablename__ = 'research'
    id = Column(Integer, primary_key=True, autoincrement=True)
    reg_number = Column(Integer)
    reg_date = Column(String)
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
    formation_date = Column(String)
    article = Column(String)
    plot = Column(String)
    incident_date = Column(String)
    address = Column(String)
