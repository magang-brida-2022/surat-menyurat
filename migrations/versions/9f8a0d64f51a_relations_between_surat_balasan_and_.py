"""relations between surat_balasan and surat_masuk

Revision ID: 9f8a0d64f51a
Revises: b7671625abf8
Create Date: 2022-09-15 17:56:02.760000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9f8a0d64f51a'
down_revision = 'b7671625abf8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('surat_balasan', sa.Column('surat_masuk_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'surat_balasan', 'surat_masuk', ['surat_masuk_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'surat_balasan', type_='foreignkey')
    op.drop_column('surat_balasan', 'surat_masuk_id')
    # ### end Alembic commands ###