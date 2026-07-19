from pydantic import BaseModel, ConfigDict, EmailStr


class PersonCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    email: EmailStr


class PersonUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone_number: str | None = None
    email: EmailStr | None = None


class PersonResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    first_name: str
    last_name: str
    phone_number: str
    email: EmailStr