"""create todos table

Revision ID: 6b3d55938bc7
Revises: 3c4050da20d4
Create Date: 2024-07-31 12:59:38.358379

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b3d55938bc7'
down_revision: Union[str, None] = '3c4050da20d4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
