from aiogram import types
from loguru import logger


async def setup_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "start"),
            types.BotCommand("help", "help"),
            types.BotCommand("email", "email"),
            types.BotCommand("statistic", "statistic"),
        ]
    )
    logger.info('Standard commands are successfully configured')
