"""create_advice_table

Revision ID: 88bf8fdc77ef
Revises: 5036a6f8d3aa
Create Date: 2023-04-17 21:55:31.636410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '88bf8fdc77ef'
down_revision = '5036a6f8d3aa'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    create table advice(
        id bigserial primary key,
        email text,
        name text,
        advice text,
        created_at timestamp
    )
    """)


def downgrade() -> None:
    op.execute("drop table advice;")
