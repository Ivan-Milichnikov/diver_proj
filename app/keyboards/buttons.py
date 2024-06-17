from aiogram.types import (ReplyKeyboardMarkup,
                           KeyboardButton,
                           InlineKeyboardMarkup,
                           inline_keyboard_button)

choice = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да"),KeyboardButton(text="Нет")]
    ],
    resize_keyboard=True
)

