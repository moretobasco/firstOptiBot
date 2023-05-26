from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from lexicon.lexicon import LEXICON, companies
from datetime import datetime
import locale

# this function creates a keyboard na letu
def creating_keyboard(width: int, *args: str, last_btn: str | None = None, **kwargs: str) -> InlineKeyboardMarkup:
    # initialize builder
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # initialize list for buttons
    buttons: list[InlineKeyboardButton] = []

    # fill the list with buttons from agruments args and kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(text=LEXICON[button] if button in LEXICON else button,
                                                callback_data=button))

    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(text=text, callback_data=button))

    # unpack list with buttons in a builder with row method with width parameter
    kb_builder.row(*buttons, width=width)

    # add in a builder last row if it had been added to function
    if last_btn:
        kb_builder.row(InlineKeyboardButton(text=last_btn, callback_data='last_btn'))

    # return an object of keyboard
    return kb_builder.as_markup()


# this function creates a list with months in Jan 21 format
def creating_months(year: int):
    month_list = []

    for i in range(1, 13):
        locale.setlocale(locale.LC_ALL, 'en_US')
        month = f"{datetime.strptime(str(i), '%m').strftime('%b')} {str(year)[-2:]}"
        month_list.append(month)

    return month_list


add_keys: InlineKeyboardButton = InlineKeyboardButton(
    text='ДОБАВИТЬ КЛЮЧИ',
    callback_data='add_keys_pressed'
)

delete_keys: InlineKeyboardButton = InlineKeyboardButton(
    text='УДАЛИТЬ КЛЮЧИ',
    callback_data='delete_keys_pressed'
)

keys_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[add_keys],
                     [delete_keys]]
)