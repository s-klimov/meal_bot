from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

confirm_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Да", callback_data="confirm"),
        InlineKeyboardButton(text="Отмена", callback_data="cancel")
    ]
])
