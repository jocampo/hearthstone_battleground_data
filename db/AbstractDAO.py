from abc import ABC

from sqlalchemy.orm import scoped_session, Session

from db.ConnectionManager import ConnectionManager


class AbstractDAO(ABC):
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
