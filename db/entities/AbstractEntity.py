import sqlalchemy.orm
from sqlalchemy.orm import declared_attr
from sqlalchemy.schema import Column
from sqlalchemy.sql import func
from sqlalchemy.types import Integer, DateTime


class AbstractEntity():
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column("id", Integer, primary_key=True)
    created_at = Column("created_at", DateTime(timezone=True), server_default=func.now())
    updated_at = Column("updated_at", DateTime(timezone=True), onupdate=func.now())
