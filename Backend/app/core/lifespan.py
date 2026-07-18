from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Sentinel AI...")

    yield

    logger.info("Stopping Sentinel AI...")