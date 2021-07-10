from abc import ABC

from sqlalchemy.orm import scoped_session, Session

from db.ConnectionManager import ConnectionManager


class AbstractDAO(ABC):
    @staticmethod
    def create(entity):
        AbstractDAO.get_connection().add(entity)

    @staticmethod
    def delete(entity):
        AbstractDAO.get_connection().delete(entity)

    @staticmethod
    def generic_get(entity):
        return (AbstractDAO.get_connection()
                .query(entity.__class__)
                .filter(entity.__class__.id == entity.id)
                .one())

    @staticmethod
    def begin():
        AbstractDAO.get_connection().begin()

    @staticmethod
    def rollback():
        AbstractDAO.get_connection().rollback()

    @staticmethod
    def commit():
        AbstractDAO.get_connection().commit()

    @staticmethod
    def get_connection() -> Session:
        return ConnectionManager().get_session()
