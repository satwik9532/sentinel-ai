from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

from app.core.logger import logger
from app.exceptions import (
    BusinessException,
    DatabaseException,
)


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(DatabaseException)
    async def database_exception_handler(
        request: Request,
        exc: DatabaseException,
    ):
        logger.exception(exc)

        return JSONResponse(
            status_code=500,
            content={
                "detail": "Database error occurred.",
            },
        )

    @app.exception_handler(BusinessException)
    async def business_exception_handler(
        request: Request,
        exc: BusinessException,
    ):
        logger.warning(str(exc))

        return JSONResponse(
            status_code=400,
            content={
                "detail": str(exc),
            },
        )

    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(
        request: Request,
        exc: SQLAlchemyError,
    ):
        logger.exception(exc)

        return JSONResponse(
            status_code=500,
            content={
                "detail": "Internal database error.",
            },
        )
