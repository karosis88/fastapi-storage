"""empty message

Revision ID: 9d0f4b8fd381
Revises: e9efa3d685f6
Create Date: 2023-03-02 09:06:29.340125

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "9d0f4b8fd381"
down_revision = "e9efa3d685f6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("storage", sa.Column("created_at", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("storage", "created_at")
    # ### end Alembic commands ###
