"""empty message

Revision ID: eb88565f117e
Revises: 756d119923eb
Create Date: 2023-03-02 08:47:42.922711

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "eb88565f117e"
down_revision = "756d119923eb"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("storage", sa.Column("maxium_space_kb", sa.Integer(), nullable=True))
    op.drop_column("storage", "maxium_space_gb")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "storage",
        sa.Column("maxium_space_gb", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.drop_column("storage", "maxium_space_kb")
    # ### end Alembic commands ###
