"""create hero table

Revision ID: 7867ef9f715d
Revises: 1554cfb6144c
Create Date: 2021-07-08 01:27:55.617773

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.

revision = '7867ef9f715d'
down_revision = '1554cfb6144c'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "hero",
        sa.Column("id", Integer, primary_key=True),
        sa.Column("thumbnail", String, nullable=False),
        sa.Column("created_at", DateTime(timezone=True), server_default=func.now()),
        sa.Column("updated_at", DateTime(timezone=True), onupdate=func.now())
    )


def downgrade():
    op.drop_table("hero")
