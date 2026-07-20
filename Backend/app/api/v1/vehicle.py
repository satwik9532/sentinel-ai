from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.schemas.vehicle import VehicleCreate, VehicleResponse
from app.services.vehicle_service import VehicleService

router = APIRouter(
    prefix="/vehicles",
    tags=["Vehicles"],
)


@router.post(
    "",
    response_model=VehicleResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_vehicle(
    payload: VehicleCreate,
    db: Session = Depends(get_db),
):
    service = VehicleService(db)

    return service.create_vehicle(payload)


@router.get(
    "",
    response_model=list[VehicleResponse],
)
def list_vehicles(
    db: Session = Depends(get_db),
):
    service = VehicleService(db)

    return service.list_vehicles()
