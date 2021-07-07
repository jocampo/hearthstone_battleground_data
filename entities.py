from dataclasses import dataclass


@dataclass
class BattlegroundMatchLog(object):
    date: str
    starting_mmr: int
    result: str
    mmr_delta: int
    hero: str
    comments: str
    last_turn: int = -1
    prize_game: bool = False

    def as_array(self):
        return [getattr(self, field) for field in self.__dataclass_fields__]
