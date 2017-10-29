"""empty message

Revision ID: ec10a5246896
Revises: 20964ae25423
Create Date: 2017-10-29 09:06:01.456813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec10a5246896'
down_revision = '20964ae25423'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('remoteusers', sa.Column('is_fmadmin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('remoteusers', 'is_fmadmin')
    # ### end Alembic commands ###