import sqlalchemy as sa
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(
        "uuid",
        sa.Uuid,
        primary_key=True,
    )
