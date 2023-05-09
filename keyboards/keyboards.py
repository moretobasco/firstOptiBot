from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, months_twentyone_ru, months_twentytwo_ru, companies, pl_lines,\
    months_twentyone_en, months_twentytwo_en

button_2021: InlineKeyboardButton = InlineKeyboardButton(
    text='2021',
    callback_data='button_2021_pressed'
)

button_2022: InlineKeyboardButton = InlineKeyboardButton(
    text='2022',
    callback_data='button_2022_pressed'
)

keyboard_years: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_2021],
                     [button_2022]]
)



def keyboard_twenty_one_en() -> InlineKeyboardMarkup:
    # initialize builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=item, callback_data=item) for item in months_twentyone_en], width=3)
    return kb_builder.as_markup()


def keyboard_twenty_two_en() -> InlineKeyboardMarkup:
    # initialize builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=item, callback_data=item) for item in months_twentytwo_en], width=3)
    return kb_builder.as_markup()


def keyboard_twenty_one() -> InlineKeyboardMarkup:
    # initialize builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=item, callback_data=item) for item in months_twentyone_ru], width=3)
    return kb_builder.as_markup()


def keyboard_twenty_two() -> InlineKeyboardMarkup:
    # initialize builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=item, callback_data=item) for item in months_twentytwo_ru], width=3)
    return kb_builder.as_markup()


def keyboard_companies() -> InlineKeyboardMarkup:
    # initialize builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=item, callback_data=item) for item in companies])
    return kb_builder.as_markup()

# оптимизировать весь модуль

def keyboard_pl() -> InlineKeyboardMarkup:
    # initialize builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(text=item, callback_data=item) for item in pl_lines])
    return kb_builder.as_markup()

