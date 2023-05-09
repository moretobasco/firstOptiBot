from aiogram import Router
from aiogram.types import CallbackQuery, Message
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon import LEXICON, months_twentyone_en, months_twentytwo_en,\
    months_twentytwo_ru, months_twentyone_ru, companies, pl_lines
from keyboards.keyboards import keyboard_years, keyboard_twenty_one_en, keyboard_twenty_two_en,\
    keyboard_twenty_one, keyboard_twenty_two, keyboard_companies, keyboard_pl
from database.database import users_choose, user_db
from copy import deepcopy
from services.opti_parser import get_info, listing


router: Router = Router()

@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON['/start'], reply_markup=keyboard_years)
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = deepcopy(users_choose)



@router.callback_query(Text(text='button_2021_pressed'))
async def twentyone_pressed(callback: CallbackQuery):
    await callback.message.answer(text='Выбери нужный месяц', reply_markup=keyboard_twenty_one_en())
    await callback.answer()


@router.callback_query(Text(text='button_2022_pressed'))
async def twentyone_pressed(callback: CallbackQuery):
    await callback.message.answer(text='Выбери нужный месяц', reply_markup=keyboard_twenty_two_en())
    await callback.answer()


@router.callback_query(lambda x: x.data in months_twentyone_en or x.data in months_twentytwo_en) # оптимизировать or
async def period_choosen(callback: CallbackQuery):
    user_db[callback.from_user.id]['month'] = callback.data
    await callback.message.answer(text='Выбери Компанию', reply_markup=keyboard_companies())
    await callback.answer()

@router.callback_query(lambda x: x.data in companies)
async def pl_choosen(callback: CallbackQuery):
    user_db[callback.from_user.id]['company'] = callback.data
    print(user_db)
    await callback.message.answer(text='Выбери статью', reply_markup=keyboard_pl())
    await callback.answer()


@router.callback_query(lambda x: x.data in pl_lines)
async def info_for_user(callback: CallbackQuery):
    user_db[callback.from_user.id]['pl'] = callback.data
    print(user_db)
    text = get_info(user_db[callback.from_user.id]['month'],
                    user_db[callback.from_user.id]['company'],
                    user_db[callback.from_user.id]['pl'])
    await callback.message.answer(text=text)
    await callback.answer()
    print(text)



# @router.callback_query(lambda x: x.data in pl_lines)
# async def info_for_user(callback: CallbackQuery):
#     user_db[callback.from_user.id]['pl'] = callback.data
#     await callback.message.answer(text=listing())
#     await callback.answer()

