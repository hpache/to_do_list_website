"""empty message

Revision ID: 2aa2e643370b
Revises: 
Create Date: 2021-11-14 12:36:17.328034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2aa2e643370b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('info_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item', sa.String(), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('priority', sa.String(), nullable=True),
    sa.Column('tag', sa.String(), nullable=True),
    sa.Column('completed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('info_table')
    # ### end Alembic commands ###
