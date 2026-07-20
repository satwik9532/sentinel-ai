from sqlalchemy.orm import Session

from app.models.person_vehicle import PersonVehicle


class PersonVehicleRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        relation: PersonVehicle,
    ):

        self.db.add(relation)

        return relation