"""create_product_images_table

Revision ID: a4477e105f53
Revises: bd081da8615b
Create Date: 2023-12-14 18:05:28.470633

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = 'a4477e105f53'
down_revision: Union[str, None] = 'bd081da8615b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# pylint: disable=no-member
# pylint doesn't find clearly existing methods like op.create_table()

def upgrade() -> None:
    op.create_table(
        "product_images",
        sa.Column('id', sa.CHAR(36), primary_key=True, nullable=False),
        sa.Column('alt', sa.String(255)),
        sa.Column('height', sa.SmallInteger),
        sa.Column('name', sa.String(50)),
        sa.Column('position', sa.SmallInteger),
        sa.Column('src', sa.String(255)),
        sa.Column('width', sa.SmallInteger),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )

def downgrade() -> None:
    op.drop_table("product_images")
