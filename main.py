import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

API_TOKEN = ""

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    in_time = State()
    out = State()
    url = State()



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    greenings = f"Hi {message.chat.username}😎, welcome"
    prefix = "I will remind you to mark the attendance‼️"
    subscribe = "Please select /subscribe to subscribe yourself"
    help = "Please select /help to get help"

    await message.reply(f"{greenings}\n{prefix}\n{subscribe}\n{help}")


@dp.message_handler(commands=['subscribe'])
async def send_welcome(message: types.Message):
    text = "Successfully subscribed!"
    await message.reply(text)

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    start = f"/start <i>to start conversation</i>\n"
    subscribe = "/subscribe <i>to subscribe yourself</i>\n"
    in_time = "/in <i>to set IN time</i>\n"
    out_time = "/out <i>to set OUT time</i>\n"
    remaning_time = "/r <i>to get reamaining time</i>\n\n"
    note = "<i>default time is set as</i>\n\n<code>IN : 8:30PM\nOUT : 5:00PM\nUTC+05:30 Colombo, Sri Lanka</code>"
    await message.reply(f"{start}{subscribe}{in_time}{out_time}{remaning_time}{note}",parse_mode='html')


@dp.message_handler(commands=['in'])
async def send_welcome(message: types.Message):
    note = "<i>default time is set as</i>\n\n<code>IN : 8:30PM\nOUT : 5:00PM\nUTC+05:30 Colombo, Sri Lanka</code>"
    msg = f"please enter time as 12-hour AM/PM format\n<code>8:30AM</code>"
    await message.reply(note)
    await message.reply(msg)

@dp.message_handler(state=Form.in_time, regexp='^[A-Z]$')
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    chat_id = message.chat.id
    await message.reply(f"Sucessfully IN time added")
    print(f"IN {message.text}")

@dp.message_handler(commands=['out'])
async def send_welcome(message: types.Message):
    note = "<i>default time is set as</i>\n\n<code>IN : 8:30PM\nOUT : 5:00PM\nUTC+05:30 Colombo, Sri Lanka</code>"
    msg = f"please enter time as 12-hour AM/PM format\n<code>5:30PM</code>"
    await message.reply(note)
    await message.reply(msg)


@dp.message_handler(state=Form.out, regexp='^[A-Z]$')
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    chat_id = message.chat.id
    await message.reply(f"Sucessfully OUT time added")
    print(f"OUT {message.text}")

@dp.message_handler(commands=['url'])
async def send_welcome(message: types.Message):
    note = "<code>at own risk</code>"
    await message.reply(note)

@dp.message_handler(state=Form.url, regexp='^[A-Z]$')
async def process_name(message: types.Message, state: FSMContext):
    await state.finish()
    chat_id = message.chat.id
    await message.reply(f"Sucessfully url added")
    print(f"URL {message.text}")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)