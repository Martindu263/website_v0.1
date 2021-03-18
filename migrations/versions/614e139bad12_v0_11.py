"""V0.11

Revision ID: 614e139bad12
Revises: c0840cc92380
Create Date: 2021-03-18 17:21:34.166717

"""

# revision identifiers, used by Alembic.
revision = '614e139bad12'
down_revision = 'c0840cc92380'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('isteacher', sa.String(length=6), nullable=True))
    op.add_column('users', sa.Column('phonenumber', sa.String(length=11), nullable=True))
    op.add_column('users', sa.Column('time_created', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    op.create_index(op.f('ix_users_phonenumber'), 'users', ['phonenumber'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_phonenumber'), table_name='users')
    op.drop_column('users', 'time_created')
    op.drop_column('users', 'phonenumber')
    op.drop_column('users', 'isteacher')
    # ### end Alembic commands ###
