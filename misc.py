import logging
from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


TOKEN = '1859214031:AAHfQqKy7Hm-sUXKJQ2dbANMU1pW4wZC7m0' #Токен бота
memory_storage = MemoryStorage()

bot = Bot(token=TOKEN,parse_mode='html')
dp = Dispatcher(bot,storage=memory_storage)
logging.basicConfig(level=logging.INFO)