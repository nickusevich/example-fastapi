"""add content column to posts table

Revision ID: f12d783d3b12
Revises: 0a08fce83320
Create Date: 2023-12-24 01:11:46.511673

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f12d783d3b12'
down_revision: Union[str, None] = '0a08fce83320'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass