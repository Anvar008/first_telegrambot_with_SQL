from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard1 = [
    [KeyboardButton(text="Еда🍔"), KeyboardButton(text="Напитки🍹")],
    [KeyboardButton(text="Добавить новое блюдо🍔")],
    [KeyboardButton(text="Добавить напиток🍹")],
    [KeyboardButton(text='Все пользователи')],
]
main_button1 = ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)

keyboard2 = [
    [KeyboardButton(text="Еда🍔"), KeyboardButton(text="Напитки🍹")],
]
main_button2 = ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)
