from sqlalchemy.schema import Column

from sqlalchemy.types import Integer, String

from db.entities.AbstractEntity import AbstractEntity


class Player(AbstractEntity):
    __tablename__ = "player"

    __battle_tag = Column("battle_tag", String(20), nullable=False)
    __current_mmr = Column("current_mmr", Integer, nullable=False)
