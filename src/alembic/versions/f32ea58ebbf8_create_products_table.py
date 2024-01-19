"""create_products_table

Revision ID: f32ea58ebbf8
Revises: 86067c157146
Create Date: 2023-12-14 16:15:18.622685

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f32ea58ebbf8'
down_revision: Union[str, None] = '86067c157146'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# pylint: disable=no-member
# pylint doesn't find clearly existing methods like op.create_table()
def upgrade() -> None:
    op.create_table(
        "products",
        sa.Column('id', sa.CHAR(36), primary_key=True, nullable=False),
        sa.Column('name', sa.String(255)),
        sa.Column('slug', sa.String(255), unique=True),
        sa.Column('sku', sa.String(50), unique=True),
        sa.Column('type', sa.String(30)),
        sa.Column('status', sa.String(30)),
        sa.Column('catalog_visibility', sa.String(30)),
        sa.Column('long_description', sa.String(255)),
        sa.Column('short_description', sa.String(255)),
        sa.Column('price', sa.String(15)),
        sa.Column('regular_price', sa.String(15)),
        sa.Column('sale_price', sa.String(15), nullable=True),
        sa.Column('sale_start_date', sa.DateTime, nullable=True),
        sa.Column('sale_end_date', sa.DateTime, nullable=True),
        sa.Column('on_sale', sa.Boolean()),
        sa.Column('total_sales', sa.Integer),
        sa.Column('virtual', sa.Boolean()),
        sa.Column('quantity', sa.Integer),
        sa.Column('sold_individually', sa.Boolean()),
        sa.Column('weight', sa.String(30)),
        sa.Column('shipping_taxable', sa.Boolean()),
        sa.Column('reviews_allowed', sa.Boolean()),
        sa.Column('average_rating', sa.Integer),
        sa.Column('rating_count', sa.Integer),
        sa.Column('related_ids', sa.String(255), nullable=True),
        sa.Column('upsells_ids', sa.String(255), nullable=True),
        sa.Column('cross_sells_ids', sa.String(255), nullable=True),
        sa.Column('parent_id', sa.String(32)),
        sa.Column('purchase_note', sa.String(255)),
        sa.Column('categories', sa.String(255)),
        sa.Column('tags', sa.String(255), nullable=True),
        sa.Column('images', sa.String(255)),
        sa.Column('attributes', sa.String(255)),
        sa.Column('variations', sa.String(255), nullable=True),
        sa.Column('menu_order', sa.Integer),
        sa.Column('metadata', sa.String(255)),
        sa.Column('created_at', sa.DateTime),
        sa.Column('updated_at', sa.DateTime)
    )


def downgrade() -> None:
    op.drop_table('products')
