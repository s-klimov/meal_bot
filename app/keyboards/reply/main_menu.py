from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from app.keyboards.reply.menu_items import menu_item

menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=menu_item["add_event"]),
            KeyboardButton(text=menu_item["del_event"]),
        ],
        [
            KeyboardButton(text=menu_item["show_day"]),
            KeyboardButton(text=menu_item["show_all"]),
        ],
        [
            KeyboardButton(text=menu_item["del_day"]),
            KeyboardButton(text=menu_item["del_day"]),
        ],
    ],
    resize_keyboard=True
)
