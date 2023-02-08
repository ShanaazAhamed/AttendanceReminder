from logging import basicConfig,INFO
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from client.request_handler import _start, _subscribed, _help, get_ids
from client.request_handler import _changein, _setin, _changeout, _setout, _addurl, _seturl, _getr
from client.helper import get_token, formattime
from client.db import DB

from datetime import date, datetime
from pytz import timezone
from apscheduler.schedulers.background import BackgroundScheduler
from asyncio import run

API_TOKEN = get_token()
basicConfig(level=INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
IN_t, OUT_t = [], []

class Form(StatesGroup):
    in_time = State()
    out = State()
    url = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    msg = _start(message.chat.username)
    await message.reply(msg, parse_mode='html')


@dp.message_handler(commands=['subscribe'])
async def subscribed(message: types.Message):
    msg = _subscribed(message.chat.id)
    await message.reply(msg, parse_mode='html')


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    msg = _help()
    await message.reply(msg, parse_mode='html')


@dp.message_handler(commands=['in'])
async def change_in(message: types.Message):
    await Form.in_time.set()
    msg = _changein(message.chat.id)
    await message.reply(msg, parse_mode='html')


@dp.message_handler(state=Form.in_time)
async def set_in(message: types.Message, state: FSMContext):
    await state.finish()
    time = formattime(message.text)
    msg = "Invalid Time!"
    if time != False:
        msg, validation = _setin(message.chat.id,time)

    await message.reply(msg, parse_mode='html')



@dp.message_handler(commands=['out'])
async def change_out(message: types.Message):
    await Form.out.set()
    msg = _changeout(message.chat.id)
    await message.reply(msg, parse_mode='html')


@dp.message_handler(state=Form.out)
async def set_out(message: types.Message, state: FSMContext):
    await state.finish()
    time = formattime(message.text)
    msg = "Invalid Time!"
    if time != False:
        msg, validation = _setout(message.chat.id, time)

    await message.reply(msg, parse_mode='html')


@dp.message_handler(commands=['url'])
async def add_url(message: types.Message):
    await Form.url.set()
    msg = _addurl(message.chat.id)
    await message.reply(msg, parse_mode='html')


@dp.message_handler(state=Form.url)
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    msg = _seturl(message.chat.id, message.text)
    await message.reply(msg, parse_mode='html')

# @dp.message_handler(commands=['r'])
# async def get_remaining(message: types.Message):
#     msg = _getr(message.chat.id)
#     await message.reply(msg)


@dp.message_handler()
async def get_remaining(message: types.Message):
    msg = "Invalid command\nTry /help"
    await message.answer(msg)


async def send_message(ids, METHOD):
    msg = f'Please mark {METHOD}'
    operator = Bot(API_TOKEN)
    print("Message sent!")
    try:
        for id in ids:
            await operator.send_message(id, msg)
        await operator.close()
    except:
        pass


def retrievtimes():
    db = DB()
    IN_t, OUT_t = db.get_times()
    return IN_t, OUT_t


def message_sender(timestamp, method):
    ids = get_ids(timestamp, method)
    run(send_message(ids, method))


def start_shedule():
    global IN_t, OUT_t
    IN_t, OUT_t = retrievtimes()
    today = date.today().weekday()
    if today != 5 and today != 6:
        timestamp = formattime(datetime.now(
            timezone('Asia/Colombo')).strftime('%I:%M%p'))
        print(IN_t, OUT_t)
        if timestamp in IN_t:
            message_sender(timestamp, "IN")
        elif timestamp in OUT_t:
            message_sender(timestamp, "OUT")


if __name__ == "__main__":
    sched = BackgroundScheduler()
    sched.add_job(start_shedule, 'interval', seconds=10)
    sched.start()
    executor.start_polling(dp, skip_updates=True)
