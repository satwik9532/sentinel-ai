from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette import status


from app.api.dependencies import get_db
from app.schemas.person import PersonCreate, PersonResponse
from app.services.person_service import PersonService

router = APIRouter(prefix="/persons", tags=["Persons"])


@router.post(
    "",
    response_model=PersonResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_person(
    payload: PersonCreate,
    db: Session = Depends(get_db),
):
    service = PersonService(db)
    return service.create_person(payload)


@router.get(
    "",
    response_model=list[PersonResponse],
)
def list_people(
    db: Session = Depends(get_db),
):
    service = PersonService(db)
    return service.list_people()