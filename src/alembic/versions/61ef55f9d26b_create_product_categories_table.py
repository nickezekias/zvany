"""create_product_categories_table

Revision ID: 61ef55f9d26b
Revises: a4477e105f53
Create Date: 2024-02-20 22:46:00.251365

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "61ef55f9d26b"
down_revision: Union[str, None] = "a4477e105f53"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

# pylint: disable=no-member
# pylint doesn't find clearly existing methods like op.create_table()


def upgrade() -> None:
    op.create_table(
        "product_categories",
        sa.Column("id", sa.CHAR(36), primary_key=True, nullable=False),
        sa.Column("name", sa.String(50), unique=True),
        sa.Column("position", sa.SmallInteger),
        sa.Column("description", sa.String(255)),
        sa.Column("parent", sa.CHAR(36)),
        sa.Column("slug", sa.String(100), unique=True),
        sa.Column("visible", sa.Boolean()),
        sa.Column("created_at", sa.DateTime),
        sa.Column("updated_at", sa.DateTime),
    )


def downgrade() -> None:
    op.drop_table("product_categories")
