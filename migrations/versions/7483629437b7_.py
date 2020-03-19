"""empty message

Revision ID: 7483629437b7
Revises: 4027f154bd9d
Create Date: 2020-03-20 00:31:56.926988

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7483629437b7'
down_revision = '4027f154bd9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('address', table_name='access')
    op.create_unique_constraint(None, 'access', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'access', type_='unique')
    op.create_index('address', 'access', ['address'], unique=True)
    # ### end Alembic commands ###