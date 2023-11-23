"""create users table

Revision ID: dc0910afd1f7
Revises: 
Create Date: 2023-11-23 12:20:44.842302

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc0910afd1f7'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.CHAR(36), primary_key=True, nullable=False),
        sa.Column('avatar', sa.String(255), nullable=True),
        sa.Column('first_name', sa.String(50), nullable=False),
        sa.Column('last_name', sa.String(50), nullable=False),
        sa.Column('email', sa.String(30), unique=True, nullable=False),
        sa.Column('phone', sa.String(30), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('token', sa.String(255), unique=True, nullable=True),
        sa.Column('email_verified_at', sa.DateTime, nullable=True),
        sa.Column('phone_verified_at', sa.DateTime, nullable=True),
        sa.Column('ID_document', sa.String(255), nullable=True),
        sa.Column('ID_document_verified_at', sa.DateTime, nullable=True),
        sa.Column("is_active", sa.Boolean, nullable=False, default=0),
        sa.Column("created_at", sa.DateTime, nullable=False),
        sa.Column("updated_at", sa.DateTime, nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_user_email"), "users", ["email"], unique=True)
    op.create_index(op.f("ix_user_phone"), "users", ["phone"], unique=True)
    op.create_index(op.f("ix_user_token"), "users", ["token"], unique=True)
    op.create_index(op.f("ix_user_id"), "users", ["id"], unique=True)


def downgrade() -> None:
    pass
