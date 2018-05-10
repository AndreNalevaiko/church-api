"""Setup inicial

Revision ID: a45cf35d6019
Revises: None
Create Date: 2018-05-10 00:18:30.085067

"""

from alembic import op, context
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a45cf35d6019'
down_revision = None


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    op.create_table('person',
                    sa.Column('id', sa.Integer, nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.Column('name', sa.String(length=256), nullable=False), sa.UniqueConstraint('name'),
                    sa.Column('phone', sa.String(length=128), nullable=True),
                    sa.Column('email', sa.String(length=128), nullable=True),
                    sa.Column('photo', sa.LargeBinary(), nullable=True),
                    sa.Column('active', sa.Boolean(), nullable=True),
                    sa.Column('occupation', sa.String(length=64), nullable=True),
                    sa.Column('created_at', sa.DateTime, nullable=False),
                    sa.Column('updated_at', sa.DateTime, nullable=True))


def schema_downgrades():
    op.drop_table('person')


def data_upgrades():
    """Add any optional data upgrade migrations here!"""
    pass


def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass
