from aiogram.contrib.middlewares.logging import LoggingMiddleware
from loguru import logger

from app.loader import dp
# from app.misc import dp
from .acl import ACLMiddleware
from .throttling import ThrottlingMiddleware


if __name__ == "app.middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
    dp.middleware.setup(ACLMiddleware())
    logger.info('Middlewares are successfully configured')
