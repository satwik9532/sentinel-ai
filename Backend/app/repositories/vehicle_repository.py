from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle
from app.repositories.base import BaseRepository


class VehicleRepository(BaseRepository):
    def __init__(self, db: Session):
        super().__init__(db)

    def create(self, vehicle: Vehicle) -> Vehicle:
        self.db.add(vehicle)
        return vehicle

    def get_by_registration(
        self,
        registration_number: str,
    ) -> Vehicle | None:
        stmt = select(Vehicle).where(Vehicle.registration_number == registration_number)
        return self.db.scalar(stmt)

    def list(self) -> list[Vehicle]:
        stmt = select(Vehicle)
        return list(self.db.scalars(stmt).all())
