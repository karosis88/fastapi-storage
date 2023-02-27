"""empty message

Revision ID: 154698e9c9d9
Revises: ef702b24c36e
Create Date: 2023-02-27 16:58:12.518814

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "154698e9c9d9"
down_revision = "ef702b24c36e"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("friends", sa.Column("created_at", sa.DateTime(), nullable=True))
    op.add_column("users", sa.Column("admin", sa.Boolean(), nullable=False))
    op.add_column("users", sa.Column("created_at", sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "created_at")
    op.drop_column("users", "admin")
    op.drop_column("friends", "created_at")
    # ### end Alembic commands ###