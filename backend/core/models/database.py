import os

from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey, Boolean, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


DATABASE_NAME = 'db_SQLite3.db'
engine = create_engine(f'sqlite:///{os.path.dirname(__file__)}\\{DATABASE_NAME}')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class BaseModel(Base):
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