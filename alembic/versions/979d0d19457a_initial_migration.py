"""Initial migration

Revision ID: 979d0d19457a
Revises: 66e426ad9de2
Create Date: 2024-11-15 22:46:46.444141

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '979d0d19457a'
down_revision: Union[str, None] = '66e426ad9de2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
