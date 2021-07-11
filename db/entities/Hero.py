from sqlalchemy.schema import Column
from sqlalchemy.types import String

from db.entities import Base


class Hero(Base):
    name = Column("name", String(200), nullable=False)
    thumbnail = Column("thumbnail", String)
