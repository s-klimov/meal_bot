from loguru import logger

from app.keyboards.reply.main_menu import menu_keyboard
from app.keyboards.reply.menu_items import menu_item
from .inline.confirm import confirm_keyboard

logger.info("Keyboards are successfully configured")
