from sqlalchemy import ForeignKey
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Boolean

from db.entities import Base
from entities import BattlegroundMatchLog


class Match(Base):
    def load_from_record(self, record: BattlegroundMatchLog):
        """
        Perform data transformations as needed and load them into the class data
        :param record: record as loaded from the CSV
        """
        self.starting_mmr = int(record.starting_mmr)
        self.mmr_delta = int(record.mmr_delta)
        self.result = record.result
        self.last_turn = int(record.last_turn)
        self.is_prize_game = bool(record.prize_game)
        self.comments = record.comments

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

    result = Column(
        "result",
        String,
        nullable=False)

    mmr_delta = Column(
        "mmr_delta",
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
