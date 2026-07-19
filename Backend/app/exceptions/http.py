from fastapi import HTTPException
from starlette.status import HTTP_404_NOT_FOUND
from starlette.status import HTTP_409_CONFLICT


class ResourceNotFoundException(HTTPException):
    def __init__(self, resource: str):
        super().__init__(
            status_code=HTTP_404_NOT_FOUND,
            detail=f"{resource} not found",
        )


class ResourceAlreadyExistsException(HTTPException):
    def __init__(self, resource: str):
        super().__init__(
            status_code=HTTP_409_CONFLICT,
            detail=f"{resource} already exists",
        )