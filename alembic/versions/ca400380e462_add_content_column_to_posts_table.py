"""add content column to posts table

Revision ID: ca400380e462
Revises: 4e00642aee06
Create Date: 2022-06-22 16:54:56.542354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ca400380e462'
down_revision = '4e00642aee06'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
        sa.Column('content', sa.String(), nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
