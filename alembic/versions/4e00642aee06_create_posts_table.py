"""create posts table

Revision ID: 4e00642aee06
Revises: 
Create Date: 2022-06-22 15:46:27.132228

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4e00642aee06'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('title', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
