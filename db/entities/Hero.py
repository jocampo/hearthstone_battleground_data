from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column

from sqlalchemy.types import String

from db.entities.AbstractEntity import AbstractEntity

Base = declarative_base(cls=AbstractEntity)


class Hero(Base):
    name = Column("name", String(200), nullable=False)
    thumbnail = Column("thumbnail", String)
