"""empty message

Revision ID: b590f62c7e1c
Revises: f3f327ab19e9
Create Date: 2017-10-14 16:00:05.224665

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b590f62c7e1c'
down_revision = 'f3f327ab19e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fullnames', sa.String(length=100), nullable=True),
    sa.Column('mobilenumber', sa.Integer(), nullable=True),
    sa.Column('nationalid', sa.Integer(), nullable=True),
    sa.Column('deptamount', sa.Integer(), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('fullnames')
    )
    op.create_index(op.f('ix_events_deptamount'), 'events', ['deptamount'], unique=False)
    op.create_index(op.f('ix_events_mobilenumber'), 'events', ['mobilenumber'], unique=True)
    op.create_index(op.f('ix_events_nationalid'), 'events', ['nationalid'], unique=True)
    op.drop_table('deptors')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('deptors',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('fullnames', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('mobilenumber', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('nationalid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('deptamount', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('description', mysql.VARCHAR(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_index(op.f('ix_events_nationalid'), table_name='events')
    op.drop_index(op.f('ix_events_mobilenumber'), table_name='events')
    op.drop_index(op.f('ix_events_deptamount'), table_name='events')
    op.drop_table('events')
    # ### end Alembic commands ###