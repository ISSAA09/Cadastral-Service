"""Fixed cadastral_number column type

Revision ID: 66e426ad9de2
Revises: e26fb13ace1a
Create Date: 2024-11-15 22:43:32.264967

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '66e426ad9de2'
down_revision: Union[str, None] = 'e26fb13ace1a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
