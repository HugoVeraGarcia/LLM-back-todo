"""create todos table

Revision ID: db061eb52d44
Revises: 3b509e3c6078
Create Date: 2024-07-31 13:36:11.481685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'db061eb52d44'
down_revision: Union[str, None] = '3b509e3c6078'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
