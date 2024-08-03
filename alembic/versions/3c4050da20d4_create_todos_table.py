"""create todos table

Revision ID: 3c4050da20d4
Revises: eb7b54a41a85
Create Date: 2024-07-31 12:26:38.878495

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3c4050da20d4'
down_revision: Union[str, None] = 'eb7b54a41a85'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
