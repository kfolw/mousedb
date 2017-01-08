"""empty message

Revision ID: fa88d22ba279
Revises: 028c4e6bd58a
Create Date: 2017-01-07 21:01:07.843927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa88d22ba279'
down_revision = '028c4e6bd58a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('logentry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('mouse_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mouse_id'], ['mouse.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('logentry')
    # ### end Alembic commands ###