from datetime import date, datetime
from sqlalchemy import func, and_, desc
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from aiogram.utils.markdown import hcode

from app.loader import dp, db
from app.models import Mealtime


# TODO отформатировать строки вывода информации
@dp.message_handler(Command("statistic", prefixes="!/"))
async def command_statistic_handler(message: types.Message):
    daily_records = await(db.select([Mealtime.meal_date, db.func.count(Mealtime.meal_date)])
                          .select_from(Mealtime)
                          .where(Mealtime.user_id == message.from_user.id)
                          .group_by(Mealtime.meal_date)
                          .order_by(desc(Mealtime.meal_date))  # сортируем по убыванию дат от текущей
                          .limit(5)  # Получаем первые 5 записей
                          .gino
                          .all())

    # daily_records = await Mealtime.query.where(Mealtime.user_id == message.from_user.id).group_by(Mealtime.meal_date).order_by(desc(Mealtime.meal_date)).limit(5).gino.first()

    entries_today = await(Mealtime.query
                          .where(and_(Mealtime.created_at >= datetime.now().date(),
                                      Mealtime.user_id == message.from_user.id))
                          .gino
                          .all())

    for record in daily_records:
        await message.answer(f"{str(record)}\n")
        print(record[0], date.today())
        if record[0] == date.today():
            await message.answer("\n".join([str(foo.created_at) for foo in entries_today]))


@dp.message_handler(Command("add", prefixes="!/"))
async def add_mealtime_event(message: types.Message):
    await Mealtime.create(user_id=message.from_user.id)

    total = await(db.select([db.func.count()])
                  .where(and_(Mealtime.created_at >= datetime.now().date(),
                              Mealtime.user_id == message.from_user.id))
                  .gino
                  .scalar())

    await message.answer('Прием пищи зафиксирован. Количество приемов пищи за сегодня - ' + hcode(total))


@dp.message_handler(Command("remove", prefixes="!/"))
async def del_mealtime_event(message: types.Message):
    # TODO реализовать удаление послденей записи за сегодня!
    await message.answer("Удалять последнюю запись я ещё не умею")
