import asyncio
import time
import logging
from aiogram import Bot, Dispatcher, executor, types

TOKEN = "6261344440:AAHuccUy6ZlzS9m_oAgGLWd01hr4SakvjsI"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

message_text = 0
message_text2 = 0
sum = message_text+message_text2

@dp.message_handler(commands=["start"])
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f'{user_id} {user_full_name} {time.asctime()}')
    await message.reply(f"Привет, {user_full_name}!\nЧтобы посмотреть функции бота, нажмите на /help")

@dp.message_handler(commands=["help"])
async def help_handler(message: types.Message):
    await message.reply(f"/final - рассчитать необходимые баллы на final")

@dp.message_handler(commands=["final"])
async def final_handler(message: types.Message):
    await message.reply(f"Введите баллы за midterm:")

@dp.message_handler(lambda message: message.text.isdigit())
async def midterm_handler(message: types.Message):
    message_text1 = message.text
    # Add your logic to handle the midterm score and calculate necessary points for the final
    await message.reply(f"Введите баллы за endterm:")

@dp.message_handler(lambda message: message.text.isdigit())
async def endterm_handler(message: types.Message):
    message_text2 = message.text
    await bot.send_message(sum)
    # Add your logic to handle the endterm score and calculate necessary points for the final
    # Send the calculated points to the chat

if __name__ == '__main__':
    executor.start_polling(dp)