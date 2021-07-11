"""add fields to the match table

Revision ID: 3bde6c021fe6
Revises: 87ffea6e4ca8
Create Date: 2021-07-10 20:42:20.975964

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import Column, String, Integer

revision = '3bde6c021fe6'
down_revision = '87ffea6e4ca8'
branch_labels = None
depends_on = None


def upgrade():
    result = Column(
        "result",
        String,
        nullable=False)

    mmr_delta = Column(
        "mmr_delta",
        Integer,
        nullable=False)
    op.add_column("match", result)
    op.add_column("match", mmr_delta)


def downgrade():
    op.drop_column("match", "result")
    op.drop_column("match", "mmr_delta")
