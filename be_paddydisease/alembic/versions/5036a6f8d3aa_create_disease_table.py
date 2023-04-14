"""create disease table

Revision ID: 5036a6f8d3aa
Revises: 
Create Date: 2023-04-03 00:08:15.674294

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5036a6f8d3aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    create table disease(
        id bigserial primary key,
        title text,
        slug text,
        type text,
        excerpt text,
        body text,
        image text null default null
    )
    """)


def downgrade() -> None:
    op.execute("drop table disease;")
