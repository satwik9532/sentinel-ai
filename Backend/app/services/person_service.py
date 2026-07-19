from sqlalchemy.orm import Session

from app.exceptions import ResourceAlreadyExistsException
from app.models.person import Person
from app.repositories.person_repository import PersonRepository
from app.schemas.person import PersonCreate


class PersonService:

    def __init__(self, db: Session):
        self.db = db
        self.repository = PersonRepository(db)

    def create_person(
        self,
        payload: PersonCreate,
    ) -> Person:

        existing = self.repository.get_by_email(payload.email)

        if existing:
            raise ResourceAlreadyExistsException("Person")

        person = Person(
            first_name=payload.first_name,
            last_name=payload.last_name,
            phone_number=payload.phone_number,
            email=payload.email,
        )

        self.repository.create(person)

        self.db.commit()

        self.db.refresh(person)

        return person

    def get_person(
        self,
        person_id: int,
    ) -> Person | None:

        return self.repository.get_by_id(person_id)

    def list_people(self):

        return self.repository.list()