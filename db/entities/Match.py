from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy import ForeignKey

from sqlalchemy.types import Integer, String, Boolean

from db.entities.AbstractEntity import AbstractEntity

Base = declarative_base(cls=AbstractEntity)


class Match(Base):

    player_id = Column(
        "player_id",
        Integer,
        ForeignKey(
            'player.id',
            name="fk_player_id",
            onupdate="RESTRICT",
            ondelete="RESTRICT"))

    hero_id = Column(
        "hero_id",
        Integer,
        ForeignKey(
            'hero.id',
            name="fk_hero_id",
            onupdate="RESTRICT",
            ondelete="RESTRICT"))

    starting_mmr = Column(
        "starting_mmr",
        Integer,
        nullable=False)

    comments = Column(
        "comments",
        String)

    last_turn = Column(
        "last_turn",
        Integer)

    is_prize_game = Column(
        "is_prize_game",
        Boolean,
        default=False)
