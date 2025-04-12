from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import WebAppInfo
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import asyncio
import json

TOKEN = "7596009023:AAHlQMsFuvapq3gcXyArxqnwwsRTvbjDJAM"

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start(message: types.Message):
    markup = ReplyKeyboardBuilder()
    markup.button(
        text='Відкрити веб сторінку',
        web_app=WebAppInfo(url='https://ivankriperua.github.io/Justsite/')
    )
    await message.answer('Привіт мій друг!', reply_markup=markup.as_markup(resize_keyboard=True))


@dp.message()
async def handle_web_app_data(message: types.Message):
    if message.web_app_data:
        data = json.loads(message.web_app_data.data)
        await message.answer(f"Name: {data["name"]}. Email: {data["email"]}. Phone: {data["phone"]}")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

async def main():
    await dp.start_polling(bot)




if __name__ == "__main__":
    asyncio.run(main())