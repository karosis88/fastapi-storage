"""empty message

Revision ID: 5a878a5c7cf6
Revises: b948eabf88e0
Create Date: 2023-03-01 17:56:37.309270

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "5a878a5c7cf6"
down_revision = "b948eabf88e0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "storage",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("owner_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["owner_id"],
            ["users.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("owner_id", name="unstorage"),
    )
    op.create_table(
        "file",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("storage_id", sa.Integer(), nullable=True),
        sa.Column("size", sa.Integer(), nullable=True),
        sa.Column("binary_data", sa.LargeBinary(), nullable=True),
        sa.ForeignKeyConstraint(
            ["storage_id"],
            ["storage.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("file")
    op.drop_table("storage")
    # ### end Alembic commands ###
