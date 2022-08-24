"""add relation on table user and suratkeluar

Revision ID: 29e22aa813cb
Revises: d01d718b5a08
Create Date: 2022-08-24 22:29:11.407465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29e22aa813cb'
down_revision = 'd01d718b5a08'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('surat_keluar', sa.Column('nama_file', sa.String(length=255), nullable=False))
    op.add_column('surat_keluar', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'surat_keluar', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'surat_keluar', type_='foreignkey')
    op.drop_column('surat_keluar', 'user_id')
    op.drop_column('surat_keluar', 'nama_file')
    # ### end Alembic commands ###
