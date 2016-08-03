"""empty message

Revision ID: 4946f05556b0
Revises: 5223fd37181c
Create Date: 2016-07-20 10:30:46.140297

"""

# revision identifiers, used by Alembic.
revision = '4946f05556b0'
down_revision = '5223fd37181c'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('accounts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('phone_no', sa.String(length=15), nullable=False),
    sa.Column('account_no', sa.String(length=20), nullable=False),
    sa.Column('account_provider', sa.String(length=150), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('accounts')
    ### end Alembic commands ###
