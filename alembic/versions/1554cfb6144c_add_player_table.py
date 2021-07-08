"""add player table

Revision ID: 1554cfb6144c
Revises: 
Create Date: 2021-07-07 23:29:14.702176

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.types import Integer, String, DateTime, Boolean


# revision identifiers, used by Alembic.
revision = '1554cfb6144c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "player",
        sa.Column("id", Integer, primary_key=True),
        sa.Column("battle_tag", String(20), nullable=False),
        sa.Column("current_mmr", Integer, nullable=False)
    )


def downgrade():
    op.drop_table("player")
