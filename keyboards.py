from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


start_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "Стоимость"),
            KeyboardButton(text = "о нас")
        ]
    ]
)

catalog_kb = InlineKeyboardMarkup(
    inline_keyboard = [
        [
            InlineKeyboardButton(text = 'small_games', callback_data= "Sgame"),
            InlineKeyboardButton(text = 'middle_games', callback_data= "Mgame"),
            InlineKeyboardButton(text = 'big_games', callback_data= "XLgame"),
            InlineKeyboardButton(text = 'Иное', callback_data= "other")
        ]
    ]
)

by_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='купить', url="http://ya.ru")
        ]
    ]
)