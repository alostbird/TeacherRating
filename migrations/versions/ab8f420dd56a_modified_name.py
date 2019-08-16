"""Modified name

Revision ID: ab8f420dd56a
Revises: ee1829637ebf
Create Date: 2019-08-16 18:00:38.822023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab8f420dd56a'
down_revision = 'ee1829637ebf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comment', sa.Column('value', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comment', 'value')
    # ### end Alembic commands ###
