import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class UserAccount(Base):
    __tablename__ = "user_accounts"

    id: Mapped[int] = mapped_column(
        sa.Integer, primary_key=True, autoincrement=True)

    user_id: Mapped[str] = mapped_column(sa.ForeignKey("users.uuid"))
    platform: Mapped[str]
    platform_user_id: Mapped[str]
