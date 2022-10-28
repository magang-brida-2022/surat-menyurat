"""empty message

Revision ID: 5e1cb2eae9fa
Revises: c7aa9563877c
Create Date: 2022-10-28 09:48:51.712935

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e1cb2eae9fa'
down_revision = 'c7aa9563877c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agenda',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tanggal', sa.DateTime(), nullable=True),
    sa.Column('waktu', sa.String(length=50), nullable=True),
    sa.Column('agenda', sa.String(length=225), nullable=False),
    sa.Column('tempat', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('agenda')
    # ### end Alembic commands ###
