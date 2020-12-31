from loguru import logger

from .errors import retry_after
from .private import start, mealtime

logger.info("Handlers are successfully configured")
