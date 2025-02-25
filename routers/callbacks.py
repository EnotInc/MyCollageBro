from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from parser import get_link 
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from buttons import CALL

import os
import keyboards as kb


rout_callbacks = Router()

class Report(StatesGroup):
    bag = State()


@rout_callbacks.callback_query(F.data.in_(['00', '01', '02', '03', '10', '11', '12', '13']))
async def get_this_week(callback: CallbackQuery):
    try:
        course = int(callback.data[1])
        week = int(callback.data[0])
        link = get_link(course=course, week=week)
        await callback.message.edit_text('Ваше Расписание:')
        await callback.message.answer_document(link)
    except:
        await callback.message.edit_text('Сорян, я не нашел рассписание :(\nЧто-то пошло не так')


@rout_callbacks.message(F.text == CALL)
async def bug_report(message: Message, state: FSMContext):
    await state.set_state(Report.bag)
    await message.answer('Опишите что у вас пошло не так, или напишите свое предложение о доработке бота', reply_markup=kb.cancel)


@rout_callbacks.message(Report.bag)
async def send_repot(message: Message, state: FSMContext):
    await message.reply("Я передал ваше сообщение разработчику.\nСпасибо за помощь в развитии пректа!", reply_markup=kb.menu)
    await message.forward(os.getenv('DEVELOPER'))
    await state.clear()


@rout_callbacks.callback_query(F.data == 'cancel')
async def cancel(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.edit_text('Запрос отменен', reply_markup=kb.menu)
    