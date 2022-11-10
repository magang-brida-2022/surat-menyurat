"""empty message

Revision ID: b36712876db0
Revises: fbd4f45bc562
Create Date: 2022-11-10 08:47:35.341624

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36712876db0'
down_revision = 'fbd4f45bc562'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bidang', sa.Column('kabid', sa.String(length=85), nullable=True))
    op.add_column('bidang', sa.Column('nip_kabid', sa.String(length=50), nullable=True))
    op.drop_column('bidang', 'kasubid')
    op.drop_column('bidang', 'nip_kasubid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bidang', sa.Column('nip_kasubid', sa.VARCHAR(length=50), autoincrement=False, nullable=True))
    op.add_column('bidang', sa.Column('kasubid', sa.VARCHAR(length=85), autoincrement=False, nullable=True))
    op.drop_column('bidang', 'nip_kabid')
    op.drop_column('bidang', 'kabid')
    # ### end Alembic commands ###
