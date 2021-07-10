from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column

from sqlalchemy.types import Integer, String

from db.entities.AbstractEntity import AbstractEntity

Base = declarative_base(cls=AbstractEntity)


class Player(Base):

    battle_tag = Column("battle_tag", String(20), nullable=False)
    current_mmr = Column("current_mmr", Integer, nullable=False)
