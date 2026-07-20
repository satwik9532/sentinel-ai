from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class Vehicle(Base, TimestampMixin):
    __tablename__ = "vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)

    registration_number: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        index=True,
    )

    manufacturer: Mapped[str] = mapped_column(String(100))

    model: Mapped[str] = mapped_column(String(100))

    color: Mapped[str] = mapped_column(String(50))