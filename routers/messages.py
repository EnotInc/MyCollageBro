from aiogram import F, Router
from aiogram.types import Message

import buttons as b
import keyboards as kb


rout_messages = Router()


time_array = ['9:00 - 10:30', '10:50 - 11:35 \n& 11:55 - 12:40', '13:00 - 14:30', '14:50 - 16:20', '16:30 - 18:00']


@rout_messages.message(F.text == b.ABOUT)
async def about(message:Message):
    await message.answer('Так, ну что я могу сказать о себе. Даже не знаю. Я тут просто для того что бы помочь тебе с расписанием в колледже. Подробнее можешь прочитать на странице гит хаба:\nhttps://github.com/EnotInc/CollegeMateBot')
 

@rout_messages.message(F.text == b.TIME)
async def get_time(message:Message):
    for i in range(0, 5):
        await message.answer('№ ' +str(i+1)+ ' Время: ' + str(time_array[i]))


@rout_messages.message(F.text == b.THIS)
async def get_this_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_this)


@rout_messages.message(F.text == b.NEXT)
async def get_next_week(message: Message):
    await message.answer('Ты на каком курсе сейчас?', reply_markup=kb.coures_next)
