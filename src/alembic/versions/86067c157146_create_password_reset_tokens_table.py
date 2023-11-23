"""create password reset tokens table

Revision ID: 86067c157146
Revises: dc0910afd1f7
Create Date: 2023-11-23 12:22:05.049256

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '86067c157146'
down_revision: Union[str, None] = 'dc0910afd1f7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'password_reset_tokens',
        sa.Column('id', sa.CHAR(36), primary_key=True, nullable=False),
        sa.Column('email', sa.String(50), nullable=False),
        sa.Column('token', sa.String(255), unique=True, nullable=False),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("used_at", sa.DateTime, nullable=True),
        sa.Column("ip_address", sa.DateTime, nullable=True),
        sa.Column("user_agent", sa.DateTime, nullable=True),
    )
    op.create_index(op.f("ix_prt_id"), "password_reset_tokens", ["id"], unique=True)
    op.create_index(op.f("ix_prt_token"), "password_reset_tokens", ["token"], unique=True)


def downgrade() -> None:
    pass
