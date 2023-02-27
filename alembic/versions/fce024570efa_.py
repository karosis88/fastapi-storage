"""empty message

Revision ID: fce024570efa
Revises: ffc5d273c738
Create Date: 2023-02-27 13:48:24.251704

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "fce024570efa"
down_revision = "ffc5d273c738"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("friends_user_id_fkey", "friends", type_="foreignkey")
    op.create_foreign_key(
        None, "friends", "users", ["user_id"], ["id"], ondelete="CASCADE"
    )
    op.alter_column("users", "username", existing_type=sa.VARCHAR(), nullable=False)
    op.alter_column("users", "password", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("users", "password", existing_type=sa.VARCHAR(), nullable=True)
    op.alter_column("users", "username", existing_type=sa.VARCHAR(), nullable=True)
    op.drop_constraint(None, "friends", type_="foreignkey")
    op.create_foreign_key(
        "friends_user_id_fkey", "friends", "users", ["user_id"], ["id"]
    )
    # ### end Alembic commands ###
