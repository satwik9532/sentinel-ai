from fastapi import APIRouter

from app.api.v1.health import router as health_router
from app.api.v1.person import router as person_router
from app.api.v1.vehicle import router as vehicle_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(health_router)
api_router.include_router(person_router)
api_router.include_router(vehicle_router)
