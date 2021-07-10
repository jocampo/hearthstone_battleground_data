import sqlalchemy
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session, sessionmaker, scoped_session

from conf.ConfigManager import ConfigManager
from utils.singleton import Singleton


class ConnectionManager(metaclass=Singleton):
    def __init__(self):
        self.__engine = create_engine(
            ConfigManager.get_db_connection_string()
        )
        self.__session = None

    def get_session(self):
        if not self.__session:
            return self.get_new_session()
        return self.__session

    def get_new_session(self):
        # TODO: in the future, when there's multiple threads, we probably shouldn't handle the session like this
        self.__session = scoped_session(sessionmaker(bind=self.__engine, autocommit=True))
        return self.__session
