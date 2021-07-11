"""make heroes thumbnail nullable

Revision ID: 87ffea6e4ca8
Revises: 9fb70fb4d41e
Create Date: 2021-07-10 19:47:24.253357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from db.AbstractDAO import AbstractDAO
from db.HeroDAO import HeroDAO

revision = '87ffea6e4ca8'
down_revision = '9fb70fb4d41e'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column("hero", "thumbnail", nullable=True)


def downgrade():
    AbstractDAO.begin()
    heroes = HeroDAO.list()
    for hero in heroes:
        if hero.thumbnail is None:
            hero.thumbnail = ""
    AbstractDAO.commit()
    op.alter_column("hero", "thumbnail", nullable=False)
