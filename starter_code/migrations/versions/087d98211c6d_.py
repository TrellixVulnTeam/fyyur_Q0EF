"""empty message

Revision ID: 087d98211c6d
Revises: 0cea980b74c1
Create Date: 2021-01-22 11:46:01.611026

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '087d98211c6d'
down_revision = '0cea980b74c1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('venue', 'seeking_venue')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('venue', sa.Column('seeking_venue', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
