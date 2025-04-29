from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.all_keyboards import menu_kb
from db_handler.db_class import Pars_from_users

start_router = Router(name="start")

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Вас приветствует ДЕМО версия телеграмм бота. \n Автор: https://github.com/Romidzeez')

# Пример работы F = " Магический фильтр ". F.text == '/start_3' == неважно что содержащее  в атребуте текст значение /start_3 

# @start_router.message(F.text == '/start_3')
# async def cmd_start_3(message: Message):
#     await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!')

@start_router.message(F.text == "test")
async def test_keyboard(message: Message):
    await message.answer("choose action:", reply_markup=menu_kb)


@start_router.message(F.text.contains('для любимки'))
async def cmd_start_4(message: Message):
    await message.answer('люблю тебя больше всего на свете моя маленька, ты самая лучшая <3')

@start_router.message(F.text.contains('all from db'))
async def all_from_db(message: Message):
    parsed = await Pars_from_users(row="*",disable_param=True,all_from=True)
    await message.answer(parsed)