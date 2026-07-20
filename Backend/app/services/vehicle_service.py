from sqlalchemy.orm import Session

from app.core.database import transaction
from app.exceptions import ResourceAlreadyExistsException
from app.models.vehicle import Vehicle
from app.repositories.vehicle_repository import VehicleRepository
from app.schemas.vehicle import VehicleCreate


class VehicleService:
    def __init__(self, db: Session):
        self.db = db
        self.repository = VehicleRepository(db)

    def create_vehicle(
        self,
        payload: VehicleCreate,
    ) -> Vehicle:

        existing = self.repository.get_by_registration(
            payload.registration_number
        )

        if existing:
            raise ResourceAlreadyExistsException("Vehicle")

        vehicle = Vehicle(
            registration_number=payload.registration_number,
            manufacturer=payload.manufacturer,
            model=payload.model,
            color=payload.color,
        )

        with transaction(self.db):
            self.repository.create(vehicle)

        self.db.refresh(vehicle)

        return vehicle

    def list_vehicles(self):
        return self.repository.list()