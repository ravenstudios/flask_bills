"""init

Revision ID: c0236b349b39
Revises: 
Create Date: 2023-10-27 16:56:55.827034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0236b349b39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bill')
    op.drop_table('paycheck')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paycheck',
    sa.Column('_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('ammount', sa.VARCHAR(length=100), nullable=True),
    sa.Column('date_paid', sa.DATE(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('bill',
    sa.Column('_id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=100), nullable=True),
    sa.Column('ammount', sa.VARCHAR(length=100), nullable=True),
    sa.Column('due_date', sa.DATE(), nullable=True),
    sa.Column('date_paid', sa.DATE(), nullable=True),
    sa.Column('is_paid', sa.BOOLEAN(), nullable=True),
    sa.Column('notes', sa.VARCHAR(length=300), nullable=True),
    sa.Column('paycheck_id', sa.INTEGER(), nullable=True),
    sa.CheckConstraint('_id'),
    sa.ForeignKeyConstraint(['paycheck_id'], ['paycheck._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###
