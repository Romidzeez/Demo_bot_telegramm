
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# Создаём клавиатуру
menu_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="all from db")],  # Первый ряд
        [KeyboardButton(text="Test")],  # Второй ряд
        # [KeyboardButton(text="Запросить контакт", request_contact=True)],  # Кнопка с запросом номера
        # [KeyboardButton(text="Запросить геолокацию", request_location=True)],  # Кнопка с геопозицией
    ],
    resize_keyboard=True,  # Подстраивает размер кнопок
    one_time_keyboard=True,  # Скрывает клавиатуру после нажатия
)