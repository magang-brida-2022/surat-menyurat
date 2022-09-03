"""init

Revision ID: 019af5f6ac56
Revises: 
Create Date: 2022-09-03 09:22:56.688757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '019af5f6ac56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bidang',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('alias', sa.String(length=50), nullable=True),
    sa.Column('nama_bidang', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('daily_activity',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('kegiatan', sa.String(length=64), nullable=False),
    sa.Column('tanggal', sa.DateTime(), nullable=False),
    sa.Column('deskripsi', sa.Text(), nullable=False),
    sa.Column('output', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('default', sa.Boolean(), nullable=True),
    sa.Column('permissions', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_role_default'), 'role', ['default'], unique=False)
    op.create_table('surat_keluar',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nomor', sa.String(length=64), nullable=True),
    sa.Column('jenis', sa.String(length=125), nullable=False),
    sa.Column('ringkasan', sa.String(length=255), nullable=False),
    sa.Column('tanggal_dikeluarkan', sa.DateTime(), nullable=True),
    sa.Column('tujuan', sa.String(length=64), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('nama_file', sa.String(length=255), nullable=False),
    sa.Column('lampiran', sa.LargeBinary(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('surat_masuk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nomor', sa.String(length=64), nullable=True),
    sa.Column('asal', sa.String(length=125), nullable=False),
    sa.Column('perihal', sa.Text(), nullable=False),
    sa.Column('tanggal_surat', sa.DateTime(), nullable=True),
    sa.Column('tanggal_diterima', sa.DateTime(), nullable=True),
    sa.Column('nama_file', sa.String(length=255), nullable=False),
    sa.Column('lampiran', sa.LargeBinary(), nullable=False),
    sa.Column('disposisi_ke', sa.String(length=50), nullable=True),
    sa.Column('dilihat', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password_hash', sa.String(length=120), nullable=True),
    sa.Column('nama', sa.String(length=50), nullable=True),
    sa.Column('jabatan', sa.String(length=35), nullable=True),
    sa.Column('no_telpon', sa.String(length=100), nullable=True),
    sa.Column('foto_profile', sa.String(length=250), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('bidang_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bidang_id'], ['bidang.id'], ),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('surat_masuk')
    op.drop_table('surat_keluar')
    op.drop_index(op.f('ix_role_default'), table_name='role')
    op.drop_table('role')
    op.drop_table('daily_activity')
    op.drop_table('bidang')
    # ### end Alembic commands ###
