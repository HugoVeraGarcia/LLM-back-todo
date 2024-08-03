"""create todos table

Revision ID: 3b509e3c6078
Revises: 70563e0f06f4
Create Date: 2024-07-31 13:20:42.803525

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3b509e3c6078'
down_revision: Union[str, None] = '70563e0f06f4'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
