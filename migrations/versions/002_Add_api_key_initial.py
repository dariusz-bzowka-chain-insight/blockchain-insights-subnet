"""Initial

Revision ID: 002_Add_api_key
Revises: 001_Initial
Create Date: 2024-08-18 19:34:42.194529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '002_Add_api_key'
down_revision: Union[str, None] = '001_Initial'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('api_keys',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk__api_keys')),
    sa.UniqueConstraint('key', name=op.f('uq__api_keys__key'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('api_keys')
    # ### end Alembic commands ###
