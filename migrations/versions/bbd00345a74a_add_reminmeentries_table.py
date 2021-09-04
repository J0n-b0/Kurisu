"""Add reminmeentries table

Revision ID: bbd00345a74a
Revises: 8441e56ee5a9
Create Date: 2021-09-03 17:24:17.300271

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bbd00345a74a'
down_revision = '8441e56ee5a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('remindmeentries',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('date', sa.TIMESTAMP(), nullable=False),
    sa.Column('author', sa.BigInteger(), nullable=False),
    sa.Column('reminder', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['author'], ['members.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('remindmeentries')
    # ### end Alembic commands ###