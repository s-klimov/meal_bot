from typing import List, Union
from contextlib import suppress
from aiogram.utils.exceptions import ChatNotFound

from loguru import logger

from app.keyboards import menu_keyboard
from app.loader import dp


async def notify_admins(admins: Union[List[int], List[str], int, str]):
    count = 0
    for admin in admins:
        with suppress(ChatNotFound):
            await dp.bot.send_message(admin, "Bot started", reply_markup=menu_keyboard)
            count += 1
    logger.info(f"{count} admins received messages")
