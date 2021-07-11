from sqlalchemy.orm import declarative_base

from db.entities.AbstractEntity import AbstractEntity

Base = declarative_base(cls=AbstractEntity)
