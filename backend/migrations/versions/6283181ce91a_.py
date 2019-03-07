"""empty message

Revision ID: 6283181ce91a
Revises: 71b60d7ec59c
Create Date: 2019-03-01 01:09:24.800520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6283181ce91a'
down_revision = '71b60d7ec59c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('counter', sa.Column('response', sa.String()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('counter', 'response')
    # ### end Alembic commands ###