from sqlalchemy.schema import Column
from sqlalchemy import ForeignKey

from sqlalchemy.types import Integer, String, Boolean

from db.entities.AbstractEntity import AbstractEntity


class Match(AbstractEntity):
    __tablename__ = "match"

    __player_id = Column(
        "player_id",
        Integer,
        ForeignKey(
            'player.id',
            name="fk_player_id",
            onupdate="RESTRICT",
            ondelete="RESTRICT"))

    __hero_id = Column(
        "hero_id",
        Integer,
        ForeignKey(
            'hero.id',
            name="fk_hero_id",
            onupdate="RESTRICT",
            ondelete="RESTRICT"))

    __starting_mmr = Column(
        "starting_mmr",
        Integer,
        nullable=False)

    _comments = Column(
        "comments",
        String)

    __last_turn = Column(
        "last_turn",
        Integer)

    __is_prize_game = Column(
        "is_prize_game",
        Boolean,
        default=False)
