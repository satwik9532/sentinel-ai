from pydantic import BaseModel, ConfigDict


class VehicleCreate(BaseModel):
    registration_number: str
    manufacturer: str
    model: str
    color: str


class VehicleResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    registration_number: str
    manufacturer: str
    model: str
    color: str
