from sqlalchemy import Column, Integer, String, Date, Boolean
from backend.core.models.database import DataBase


class Research(DataBase):
    __tablename__ = 'research'
    id = Column(Integer, primary_key=True, autoincrement=True)
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

