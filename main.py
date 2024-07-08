import asyncio
import logging

import aiogram
import executor

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from keyboards import *
import config
import text

logging.basicConfig(level=logging.INFO)

bot = Bot(token = "7354419811:AAEk3KUNZVBZTXqT3mGGq5OKCnS79XkrFeI")

dp = Dispatcher(storage = MemoryStorage())

@dp.message_handler(commands=["start"])
async  def start(message):
    await message.nswer(text.start, reply_markup= start_kb)

@dp.message_handler(txt = 'о нас')
async def info(message):
    await message.answer(text.about, replay_markup = start_kb)

@dp.message_handler(text = 'Стоимость')
async def price(message):
    await message.answer("что вам угодно?",  reply_markup=catalog_kb)
    await message.answer(text.about, replay_markup = start_kb)

@dp.callback_query_handler(text="Sgames")
async def buy_s(call):
    await call.message.answer(text.Lgame, reply_markup = by_kb)
    await call.answer()

@dp.callback_query_handler(text="Mgames")
async def buy_m(call):
    await call.message.answer(text.Mgame, reply_markup = by_kb)
    await call.answer()
@dp.callback_query_handler(text="XLgames")
async def buy_x(call):
    await call.message.answer(text.XLgame, reply_markup = by_kb)
    await call.answer()
@dp.callback_query_handler(text='other')

async def buy_other(call):
    await call.message.answer(text.other, reply_markup = by_kb)
    await call.answer()

if __name__ == "__main__":
    executor.start_pollin(dp, skip_updates = True)