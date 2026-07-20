from datetime import date

from pydantic import BaseModel


class AssignVehicleRequest(BaseModel):
    vehicle_id: int
    relationship_type: str
    start_date: date