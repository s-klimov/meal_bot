from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.keyboards.reply.callback_data import statistic_actions

statistic_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=statistic_actions["cancel"]),
            KeyboardButton(text=statistic_actions["del_all"]),
            KeyboardButton(text=statistic_actions["del_day"])
        ],
    ],
    resize_keyboard=True
)