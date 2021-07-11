from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from db.entities import Base


class Player(Base):
    battle_tag = Column("battle_tag", String(20), nullable=False)
    current_mmr = Column("current_mmr", Integer, nullable=False)
