"""add match table

Revision ID: d299ab01b505
Revises: 22b2c5cce066
Create Date: 2021-07-08 02:03:39.236525

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.types import Integer, String, DateTime, Boolean
from sqlalchemy.sql import func
from sqlalchemy import ForeignKey


# revision identifiers, used by Alembic.
revision = 'd299ab01b505'
down_revision = '22b2c5cce066'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "match",
        sa.Column("id", Integer, primary_key=True),
        sa.Column("player_id", Integer, ForeignKey('player.id', name="fk_player_id", onupdate="RESTRICT", ondelete="RESTRICT")),
        sa.Column("hero_id", Integer, ForeignKey('hero.id', name="fk_hero_id", onupdate="RESTRICT", ondelete="RESTRICT")),
        sa.Column("starting_mmr", Integer, nullable=False),
        sa.Column("comments", String),
        sa.Column("last_turn", Integer),
        sa.Column("is_prize_game", Boolean, default=False),
        sa.Column("created_at", DateTime(timezone=True), server_default=func.now()),
        sa.Column("updated_at", DateTime(timezone=True), onupdate=func.now()),
    )


def downgrade():
    op.drop_table("match")
