from sqlalchemy.schema import Column

from sqlalchemy.types import String

from db.entities.AbstractEntity import AbstractEntity


class Hero(AbstractEntity):
    __tablename__ = "hero"

    __thumbnail = Column("thumbnail", String, nullable=False)
