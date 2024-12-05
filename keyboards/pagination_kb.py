from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON

# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(*buttons:str)->InlineKeyboardMarkup:
    # Инициализируем билдер
    kp_builder=InlineKeyboardBuilder()
    # Добавляем в билдер ряд с кнопками
    kp_builder.row(*[InlineKeyboardButton(
        text=LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons]
    )
    # Возвращаем объект инлайн-клавиатуры
    return kp_builder.as_markup()

