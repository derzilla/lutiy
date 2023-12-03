import asyncio
import logging
from aiogram import Bot
from aiogram import types
from aiogram import Dispatcher

token = 'your token'
bot = Bot(token=token)
dp = Dispatcher()

@dp.message
async def saveis(message: types.Message):

	buttons = types.ReplyKeyboardMarkup()
	button1 = types.KeyboardButton('♻Как спасти планету?♻')
	buttons.add(button1)
	
async def main():
	
	logging.basicConfig(level=logging.INFO)
	await dp.start_polling(bot)
	
if __name__ == '__main__':
	asyncio.run(main())
