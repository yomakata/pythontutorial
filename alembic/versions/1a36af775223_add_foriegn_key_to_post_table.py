"""add foriegn-key to post table

Revision ID: 1a36af775223
Revises: 20b5ee91c868
Create Date: 2022-06-22 17:23:57.504635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a36af775223'
down_revision = '20b5ee91c868'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
        sa.Column('owner_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
