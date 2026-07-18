import sys
from pathlib import Path

from loguru import logger

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

logger.remove()

logger.add(
    sys.stdout,
    level="INFO",
    format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
    "<level>{level}</level> | "
    "{message}",
)

logger.add(
    LOG_DIR / "sentinel.log",
    rotation="10 MB",
    retention="10 days",
    compression="zip",
    level="INFO",
    enqueue=True,
)

__all__ = ["logger"]
