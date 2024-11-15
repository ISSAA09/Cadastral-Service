"""Initial migration

Revision ID: 0a8f353122b7
Revises: 979d0d19457a
Create Date: 2024-11-15 22:50:20.800244

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a8f353122b7'
down_revision: Union[str, None] = '979d0d19457a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
