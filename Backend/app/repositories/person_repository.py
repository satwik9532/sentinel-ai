from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.person import Person


class PersonRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, person: Person) -> Person:
        self.db.add(person)
        return person

    def get_by_id(self, person_id: int) -> Person | None:
        stmt = select(Person).where(Person.id == person_id)
        return self.db.scalar(stmt)

    def get_by_email(self, email: str) -> Person | None:
        stmt = select(Person).where(Person.email == email)
        return self.db.scalar(stmt)

    def list(self) -> list[Person]:
        stmt = select(Person)
        return list(self.db.scalars(stmt).all())