"""create_product_attributes_table

Revision ID: bd081da8615b
Revises: f32ea58ebbf8
Create Date: 2023-12-14 17:31:08.828516

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'bd081da8615b'
down_revision: Union[str, None] = 'f32ea58ebbf8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# pylint: disable=no-member
# pylint doesn't find clearly existing methods like op.create_table()

def upgrade() -> None:
    op.create_table(
        "product_attributes",
        sa.Column('id', sa.CHAR(36), primary_key=True, nullable=False),
        sa.Column('name', sa.String(30), unique=True),
        sa.Column('position', sa.SmallInteger),
        sa.Column('values', sa.String(255)),
        sa.Column('variation', sa.Boolean()),
        sa.Column('visible', sa.Boolean()),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table("product_attributes")
