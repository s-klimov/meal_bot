from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher.filters.builtin import Command
from aiogram.utils.markdown import hcode

from app.loader import dp
from app.models import User


@dp.message_handler(CommandStart())
async def command_start_handler(message: types.Message, state: FSMContext):
    user_id = message.from_user.id

    user = await User.get(user_id)

    await message.answer(
        "\n".join(
            [
                f'Привет, {message.from_user.full_name}!',
                f'Я отслеживаю статистику приемов пищи,',
                f'не забывай после каждого приема пищи присылать мне {hcode("+")}',
             ]),
     )


@dp.message_handler(Command("email", prefixes="!/"))
async def command_email_handler(message: types.Message, state: FSMContext):
    await message.answer("Пришли мне свой имейл")
    await state.set_state("email")


@dp.message_handler(state="email")
async def enter_email(message: types.Message, state: FSMContext):
    email = message.text
    user_id = message.from_user.id
    user = await User.get(user_id)
    await user.update(email=email).apply()
    await state.finish()

    await message.answer("Данные обновлены. Твой новый email \n" +
                         hcode(user.email))
