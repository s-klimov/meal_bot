from aiogram import types
from loguru import logger


async def setup_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Начать работу"),
            types.BotCommand("help", "Показать перечень команд"),
            types.BotCommand("email", "Установить/сменить email"),
            types.BotCommand("statistic", "Статистика"),
            types.BotCommand("add", "Добавить запись о приеме пищи"),
            types.BotCommand("remove", "Удалить последнюю запись о приеме пищи"),
        ]
    )
    logger.info('Standard commands are successfully configured')
