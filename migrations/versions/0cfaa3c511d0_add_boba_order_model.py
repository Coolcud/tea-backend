"""Add Boba_Order model

Revision ID: 0cfaa3c511d0
Revises: 
Create Date: 2023-07-21 12:08:26.345936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cfaa3c511d0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('boba__order',
    sa.Column('order_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('base', sa.String(), nullable=True),
    sa.Column('toppings', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('temp', sa.String(), nullable=True),
    sa.Column('sweetness', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('boba__order')
    # ### end Alembic commands ###