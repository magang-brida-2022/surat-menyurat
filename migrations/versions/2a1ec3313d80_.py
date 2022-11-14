"""empty message

Revision ID: 2a1ec3313d80
Revises: 811d94144ae0
Create Date: 2022-11-12 23:57:42.383176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a1ec3313d80'
down_revision = '811d94144ae0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sub_bidang', sa.Column('bidang_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'sub_bidang', 'bidang', ['bidang_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'sub_bidang', type_='foreignkey')
    op.drop_column('sub_bidang', 'bidang_id')
    # ### end Alembic commands ###