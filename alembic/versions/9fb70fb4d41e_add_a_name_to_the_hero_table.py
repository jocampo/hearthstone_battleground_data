"""add a name to the hero table

Revision ID: 9fb70fb4d41e
Revises: d299ab01b505
Create Date: 2021-07-10 19:43:43.901744

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.types import String


# revision identifiers, used by Alembic.

revision = '9fb70fb4d41e'
down_revision = 'd299ab01b505'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("hero", sa.Column("name", String(100), nullable=False))


def downgrade():
    op.drop_column("hero", "name")
