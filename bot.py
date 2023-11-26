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

	txt = message.text
	if txt == '/saveis':
		await message.reply('We must save the Earth from global warming by any means possible, so that we can live better')
							
async def main():
	
	logging.basicConfig(level=logging.INFO)
	await dp.start_polling(bot)
	
if __name__ == '__main__':
	asyncio.run(main())
