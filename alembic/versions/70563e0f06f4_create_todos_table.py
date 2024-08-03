"""create todos table

Revision ID: 70563e0f06f4
Revises: 6b3d55938bc7
Create Date: 2024-07-31 13:19:56.785374

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '70563e0f06f4'
down_revision: Union[str, None] = '6b3d55938bc7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
