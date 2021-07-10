from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column

from sqlalchemy.types import String

from db.entities.AbstractEntity import AbstractEntity

Base = declarative_base(cls=AbstractEntity)


class Hero(Base):

    thumbnail = Column("thumbnail", String, nullable=False)
