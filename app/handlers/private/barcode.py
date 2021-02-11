from aiogram import types
from app.loader import dp, db

# QR Code
from pyzbar.pyzbar import decode

import os
from PIL import Image


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_photo(message: types.Message):

    # id_img = await message.photo[-1].file_id
    await message.photo[-1].download('qrcode.jpg')

    try:
        result = decode(Image.open('qrcode.jpg'))
        await message.reply(result[0].data.decode("utf-8"))
        os.remove("qrcode.jpg")
    except Exception as err:
        await message.reply('Не могу распознать на картинке штрих-код. Попробуй ещё раз!\n')
