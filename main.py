import logging
import sms_module
import call_module
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = 'YOUR_TOKEN'
lst = []
white_list = [
    "YOUR_NUMBER",
]
logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply( 
        "Hi!\n"
        "I'm Fire spamming Bot!\n"
        "I have been made by DimonBor.\n"
        "<i>Check /help to learn how to use me.</i>"
        )


@dp.message_handler(commands=['help'])
async def show_help(message):
    await message.reply(
        "I see that you want to know, how it works.\n"
        "Well:\n"
        "1.Call Service. Light troll))).\n"
        "<b>    Usage:</b>\n"
        "<i>    /call YOUR_NUMBER</i>\n"
        "2.SMS service. Most powerful weapon\n"
        "<b>    Usage:</b>\n"
        "<i>    /sms YOUR_NUMBER INTERATONS</i>\n"
        "<i>    Example: /sms 0991112222 20</i>\n"
        "P.S Iterations must be less then 20."
    )


@dp.message_handler(commands=['call'])
async def call_service_cmd(message):
    num = message.get_args()
    if num in white_list:
        await message.reply("Yeah, NO! This number in White List.")
        return
    await message.reply(f'Someone calling youuuuuu)))),{num}')
    call_module.call_service(num)


@dp.message_handler(commands=['sms'])
async def sms_service_cmd(message):
    string = str(message.get_args())
    element = str()
    for i in string:
        if str(i) != " ":
            element += str(i)
        else:
            lst.append(element)
            element = str("")
    lst.append(element)
    num = lst[0]
    iterations = int(lst[1])
    if iterations > 20:
        iterations = 20
    await message.reply(f'Starting SMS Srevice for \n {num}')
    sms_module.sms_service(num, iterations)


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text, reply=False)

executor.start_polling(dp, skip_updates=True)
