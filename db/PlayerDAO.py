from db.AbstractDAO import AbstractDAO
from db.entities.Player import Player


class PlayerDAO(AbstractDAO):

    @staticmethod
    def get(player_id: int) -> Player:
        return (PlayerDAO.get_connection()
                .query(Player)
                .filter(Player.id == player_id)
                .one())
