from loguru import logger

from app.keyboards.reply.statistic import statistic_keyboard
from app.keyboards.reply.callback_data import statistic_actions
from .inline.confirm import confirm_keyboard

logger.info("Keyboards are successfully configured")
