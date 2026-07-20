from datetime import date
from enum import Enum

from sqlalchemy import Boolean, Date, Enum as SqlEnum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin


class RelationshipType(str, Enum):
    OWNER = "OWNER"
    DRIVER = "DRIVER"
    LESSEE = "LESSEE"


class PersonVehicle(Base, TimestampMixin):
    __tablename__ = "person_vehicles"

    id: Mapped[int] = mapped_column(primary_key=True)

    person_id: Mapped[int] = mapped_column(
        ForeignKey("persons.id", ondelete="CASCADE")
    )

    vehicle_id: Mapped[int] = mapped_column(
        ForeignKey("vehicles.id", ondelete="CASCADE")
    )

    relationship_type: Mapped[RelationshipType] = mapped_column(
        SqlEnum(RelationshipType)
    )

    start_date: Mapped[date] = mapped_column(Date)

    end_date: Mapped[date | None] = mapped_column(Date)

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )