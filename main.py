import logging
import threading
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from client.request_handler import _start,_subscribed,_help
from client.request_handler import _changein,_setin,_changeout,_setout,_addurl,_seturl,_getr
from client.helper import get_token
from datetime import date


API_TOKEN = get_token()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage) 
IN_t,OUT_t = [],[]

class Form(StatesGroup):
    in_time = State()
    out = State()
    url = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    msg = _start(message.chat.username)
    await message.reply(msg,parse_mode='html')


@dp.message_handler(commands=['subscribe'])
async def subscribed(message: types.Message):
    msg = _subscribed(message.chat.id)
    await message.reply(msg,parse_mode='html')

@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    msg = _help()
    await message.reply(msg,parse_mode='html')


@dp.message_handler(commands=['in'])
async def change_in(message: types.Message):
    await Form.in_time.set()
    msg = _changein(message.chat.id)
    await message.reply(msg,parse_mode='html')

@dp.message_handler(state=Form.in_time)
async def set_in(message: types.Message, state: FSMContext):
    await state.finish()
    msg,validation = _setin(message.chat.id, message.text)
    await message.reply(msg,parse_mode='html')

@dp.message_handler(commands=['out'])
async def change_out(message: types.Message):
    await Form.out.set()
    msg,validation = _changeout(message.chat.id)
    await message.reply(msg,parse_mode='html')

@dp.message_handler(state=Form.out)
async def set_out(message: types.Message, state: FSMContext):
    await state.finish()
    msg = _setout(message.chat.id, message.text)
    await message.reply(msg,parse_mode='html')

@dp.message_handler(commands=['url'])
async def add_url(message: types.Message):
    await Form.url.set()
    msg = _addurl(message.chat.id)
    await message.reply(msg,parse_mode='html')

@dp.message_handler(state=Form.url)
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    msg = _seturl(message.chat.id, message.text)
    await message.reply(msg,parse_mode='html')

# @dp.message_handler(commands=['r'])
# async def get_remaining(message: types.Message):
#     msg = _getr(message.chat.id)
#     await message.reply(msg)

@dp.message_handler()
async def get_remaining(message: types.Message):
    msg = "Invalid command\nTry /help"
    await message.answer(msg)

def get_credentials():
    load_dotenv()
    API_TOKEN = getenv("TOKEN")
    KEY = getenv("KEY")

def start_telegram():
    executor.start_polling(dp, skip_updates=True)

def start_shedule():
    global IN_t,OUT_t
    today = date.today().weekday()
    if today != 5 and today != 6:
        timestamp = time.strftime("%I:%M%p")
        print(timestamp)




if __name__ == "__main__": 
    t1 = threading.Thread(target=start_telegram)
    t2 = threading.Thread(target=start_shedule)
    t1.start()
    t2.start()