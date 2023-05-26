from aiogram import Router, Bot
from aiogram.types import CallbackQuery, Message, FSInputFile
from aiogram.filters import CommandStart, Text
from lexicon.lexicon import LEXICON, years, companies, clear_history_button, confirm_button
from keyboards.keyboards import creating_keyboard, creating_months
from database.database import users_choose, user_db
from copy import deepcopy
from services.opti_parser import parsed_data
from openai_connection.chatgpt import chatgpt_response

router: Router = Router()


# this handler will be called when /start button is pressed,
# adding user`s id to the DB
@router.message(CommandStart())
async def process_start_command(message: Message, bot: Bot):
    logo = FSInputFile('images/logo.png')
    await bot.send_photo(chat_id=message.chat.id, photo=logo)
    await message.answer(text=LEXICON['/start'], reply_markup=creating_keyboard(1, **years))
    if message.from_user.id not in user_db:
        user_db[message.from_user.id] = deepcopy(users_choose)


# this handler will be called then YEAR 2021 is pressed,
# sending the keyboard with months of 2021
@router.callback_query(Text(text='button_2021_pressed'))
async def twentyone_pressed(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери нужный месяц',
        reply_markup=creating_keyboard(3, *creating_months(2021)))
    await callback.answer()


# this handler will be called then YEAR 2022 is pressed,
# sending the keyboard with months of 2022
@router.callback_query(Text(text='button_2022_pressed'))
async def twentyone_pressed(callback: CallbackQuery):
    await callback.message.edit_text(
        text='Выбери нужный месяц',
        reply_markup=creating_keyboard(3, *creating_months(2022)))
    await callback.answer()


@router.callback_query(lambda x: x.data in creating_months(2021) or x.data in creating_months(2022))
async def month_choosen(callback: CallbackQuery):
    user_db[callback.from_user.id]['month'] = callback.data
    await callback.message.edit_text(text='Выбери Компанию, или Итого по Группе',
                                     reply_markup=creating_keyboard(3, *companies))
    await callback.answer()


@router.callback_query(lambda x: x.data in companies)
async def company_choosen(callback: CallbackQuery):
    user_db[callback.from_user.id]['company'] = callback.data
    await callback.message.edit_text(text=LEXICON['attention'],
                                     reply_markup=creating_keyboard(1, **confirm_button))
    await callback.answer()


@router.callback_query(Text(text='confirm_button_pressed'))
async def pl_choosen(callback: CallbackQuery):
    try:
        text = await parsed_data(user_db[callback.from_user.id]['month'], user_db[callback.from_user.id]['company'])
        await callback.message.edit_text(text=text,
                                         reply_markup=creating_keyboard(1, **clear_history_button))

    except:
        await callback.message.edit_text(text='СОРРИ')
    await callback.answer()


@router.callback_query(Text(text='clear_history_button_pressed'))
async def clear_history(callback: CallbackQuery):
    await callback.message.delete()
    await callback.answer()

@router.message()
async def chatgpt(message: Message):
    text = chatgpt_response(message.text)
    await message.answer(text=text)

# @router.callback_query(lambda x: x.data in pl_lines)
# async def info_for_user(callback: CallbackQuery):
#     user_db[callback.from_user.id]['pl'] = callback.data
#     print(user_db)
#     text = parsed_data(user_db[callback.from_user.id]['month'], user_db[callback.from_user.id]['company'])
#     await callback.message.answer(text=text)
#     await callback.answer()


# @router.message(Text(text='обновление ключей'))
# async def process_start_command(message: Message, bot: Bot):
#     await message.answer(text='сделай действие',reply_markup=keys_keyboard)
