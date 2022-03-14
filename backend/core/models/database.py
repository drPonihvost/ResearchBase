import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.core.settings import settings

engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

DataBase = declarative_base()


def init_db():
    if not os.path.exists(settings.DATABASE_URI):
        DataBase.metadata.create_all(engine)
    else:
        DataBase.metadata.create_all(engine)
