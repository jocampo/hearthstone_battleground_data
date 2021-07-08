"""update player table with timestamps

Revision ID: 22b2c5cce066
Revises: 7867ef9f715d
Create Date: 2021-07-08 01:31:38.059623

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.types import DateTime
from sqlalchemy.sql import func

# revision identifiers, used by Alembic.
revision = '22b2c5cce066'
down_revision = '7867ef9f715d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("player", sa.Column("created_at", DateTime(timezone=True), server_default=func.now()))
    op.add_column("player", sa.Column("updated_at", DateTime(timezone=True), onupdate=func.now()))


def downgrade():
    op.drop_column("player", "created_at")
    op.drop_column("player", "updated_at")
