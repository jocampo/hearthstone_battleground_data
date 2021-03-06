from db.AbstractDAO import AbstractDAO
from db.entities.Hero import Hero


class HeroDAO(AbstractDAO):

    @staticmethod
    def get(hero_id: int) -> Hero:
        return (HeroDAO.get_connection()
                .query(Hero)
                .filter(Hero.id == hero_id)
                .one())

    @staticmethod
    def get_by_name(hero_name: str) -> Hero:
        return (HeroDAO.get_connection()
                .query(Hero)
                .filter(Hero.name == hero_name)
                .one())

    @staticmethod
    def list() -> list[Hero]:
        return [x for x in HeroDAO.get_connection().query(Hero).all()]
