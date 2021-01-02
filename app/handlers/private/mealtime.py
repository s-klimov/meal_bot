from datetime import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.markdown import hcode

from app.keyboards import menu_keyboard, confirm_keyboard, menu_item
from app.loader import dp
from app.models import Mealtime


# TODO выводить количество приемов пищи за день
@dp.message_handler(Command("statistic", prefixes="!/"))
async def command_statistic_handler(message: types.Message):
    items = await Mealtime.query.where(Mealtime.user_id == message.from_user.id).gino.all()

    await message.answer("\n".join([str(item.created_at.date()) for item in items]),
                         reply_markup=menu_keyboard)


@dp.message_handler(Text(equals=[menu_item["del_all"], menu_item["del_day"]]))
async def get_food(message: types.Message, state: FSMContext):
    await message.answer(f"Ты хочешь {message.text}", reply_markup=ReplyKeyboardRemove())
    await message.answer(f"Точно выполняем?", reply_markup=confirm_keyboard)
    await state.set_state("delete_statistic")


# TODO реализовать двойное подтверждение удаления статистики
@dp.callback_query_handler(text="cancel", state="delete_statistic")
async def cancel_handler(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("ты отменил действие", reply_markup=None)
    await state.finish()


@dp.callback_query_handler(text="confirm", state="delete_statistic")
async def cancel_handler(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("ты подтвердил действие", reply_markup=None)
    await state.finish()


@dp.message_handler(Text(equals=[menu_item["add_event"]]))
async def add_mealtime_event(message: types.Message):
    await Mealtime.create(user_id=message.from_user.id)

    # TODO выводить количество записей по условию согласно рекомендаций SQLAlchemy
    count = await Mealtime.query.where(Mealtime.created_at >= datetime.now().date()).gino.all()
    count = len(count)
    await message.answer('Количество приемов пищи за сегодня - ' + hcode(count))


@dp.message_handler(Text(equals=[menu_item["del_event"]]))
async def del_mealtime_event(message: types.Message):

    # TODO реализовать удаление послденей записи за сегодня!
    await message.answer("Этого я ещё не умею")

    # else:
    #     await message.answer(f'Я тебя не понимаю. Введи {hcode("+")}, либо занимайся своими делами)')
