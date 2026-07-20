from fastapi import FastAPI

from app.api.router import api_router
from app.config import settings
from app.core.lifespan import lifespan
from app.core.exceptions import register_exception_handlers
from app.middleware.logging import LoggingMiddleware


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    lifespan=lifespan,
)
register_exception_handlers(app)
app.include_router(api_router)
app.add_middleware(
    LoggingMiddleware,
)


@app.get("/")
def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
    }
