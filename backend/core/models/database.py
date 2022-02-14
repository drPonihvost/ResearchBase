import os
from typing import Generator

from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.core.settings import settings

engine = create_engine(settings.DATABASE_URI)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

DataBase = declarative_base()


class DataBaseModel(DataBase):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)

    @classmethod
    def get_all(cls):
        return session.query(cls).all()

    @classmethod
    def get_by_id(cls, item_id):
        return session.query(cls).get(item_id)

    def save(self, commit=True):
        session.add(self)
        if commit:
            try:
                session.commit()
            except Exception as e:
                session.rollback()
                raise e
        return self

    @staticmethod
    def update():
        session.commit()

    def delete(self, commit=True):
        session.delete(self)
        if commit:
            try:
                session.commit()
            except Exception as e:
                session.rollback()
                raise e

    @staticmethod
    def bulk_delete(objects: list):
        for obj in objects:
            session.delete(obj)
        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e


def init_db():
    if not os.path.exists(settings.DATABASE_URI):
        DataBase.metadata.create_all(engine)
    else:
        DataBase.metadata.create_all(engine)


# Dependency injection
def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
