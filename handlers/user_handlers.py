from aiogram import Router, Bot
from aiogram.types import CallbackQuery, Message, FSInputFile
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon import LEXICON, months_twentyone_en, months_twentytwo_en,\
    months_twentytwo_ru, months_twentyone_ru, companies, pl_lines
from keyboards.keyboards import keyboard_years, keyboard_twenty_one_en, keyboard_twenty_two_en,\
    keyboard_twenty_one, keyboard_twenty_two, keyboard_companies, keyboard_pl, keyboard_back_to_years,\
    keyboard_back_to_companies, keyboard_clear_history, keyboard_confirm
from database.database import users_choose, user_db
from copy import deepcopy
from services.opti_parser import get_info, listing, parsed_data
from aiogram.methods import SendPhoto

router: Router = Router()

# this handler will be called when /start button is pressed,
# adding user`s id to the DB
@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):
    logo = FSInputFile('images/logo.png')
    await bot.send_photo(chat_id=message.chat.id, photo=logo)
    await message.answer(text=LEXICON['/start'], reply_markup=keyboard_years)
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = deepcopy(users_choose)


# this handler will be called then YEAR 2021 is pressed,
# sending the keyboard with months of 2021
@router.callback_query(Text(text='button_2021_pressed'))
async def twentyone_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text='Выбери нужный месяц', reply_markup=keyboard_twenty_one_en())
    await callback.answer()

# this handler will be called then YEAR 2022 is pressed,
# sending the keyboard with months of 2022
@router.callback_query(Text(text='button_2022_pressed'))
async def twentyone_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text='Выбери нужный месяц', reply_markup=keyboard_twenty_two_en())
    await callback.answer()


@router.callback_query(lambda x: x.data in months_twentyone_en or x.data in months_twentytwo_en)
async def pl_choosen(callback: CallbackQuery):
    user_db[callback.from_user.id]['month'] = callback.data
    await callback.message.edit_text(text='Выбери Компанию', reply_markup=keyboard_companies())
    await callback.answer()

@router.callback_query(lambda x: x.data in companies)
async def company_choosen(callback: CallbackQuery):
    user_db[callback.from_user.id]['company'] = callback.data
    print(user_db)
    # text = parsed_data(user_db[callback.from_user.id]['month'], user_db[callback.from_user.id]['company'])
    await callback.message.edit_text(text=LEXICON['attention'], reply_markup=keyboard_confirm)
    await callback.answer()


@router.callback_query(Text(text='confirm_button_pressed'))
async def pl_choosen(callback: CallbackQuery):
    text = parsed_data(user_db[callback.from_user.id]['month'], user_db[callback.from_user.id]['company'])
    await callback.message.edit_text(text=text, reply_markup=keyboard_clear_history)
    await callback.answer()

@router.callback_query(Text(text='clear_history_button_pressed'))
async def clear_history(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()

# @router.callback_query(lambda x: x.data in pl_lines)
# async def info_for_user(callback: CallbackQuery):
#     user_db[callback.from_user.id]['pl'] = callback.data
#     print(user_db)
#     text = parsed_data(user_db[callback.from_user.id]['month'], user_db[callback.from_user.id]['company'])
#     await callback.message.answer(text=text)
#     await callback.answer()




