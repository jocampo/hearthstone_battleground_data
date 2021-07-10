from db.AbstractDAO import AbstractDAO
from db.entities.Player import Player


class PlayerDAO(AbstractDAO):

    @staticmethod
    def create(player: Player):
        PlayerDAO.get_connection().add(player)

    @staticmethod
    def get(player_id: int) -> Player:
        return (PlayerDAO.get_connection()
                .query(Player)
                .filter(Player.id == player_id)
                .one())
