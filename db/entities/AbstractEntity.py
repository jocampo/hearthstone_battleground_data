import sqlalchemy.orm
from sqlalchemy.schema import Column
from sqlalchemy.sql import func
from sqlalchemy.types import Integer, DateTime

Base = sqlalchemy.orm.declarative_base()


class AbstractEntity(Base):
    __id = Column("id", Integer, primary_key=True)
    __created_at = Column("created_at", DateTime(timezone=True), server_default=func.now())
    __updated_at = Column("updated_at", DateTime(timezone=True), onupdate=func.now())
