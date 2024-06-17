from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import text
from utils import send_message_to_user,bot
from aiogram.fsm.context import FSMContext
from app.fsm.states import StartQuestion

from datetime import date

from app.database.users import User
from app.keyboards import buttons

router = Router()

"""async def send_message_to_user(user_id, message):
    try:
        await bot.send_message(chat_id=user_id, text=message)
        print(f"Сообщение отправлено пользователю с ID {user_id}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")"""

@router.message(CommandStart())
async def start_handler1(message: Message):
    await message.answer(text.greet.format(name=message.from_user.full_name))
    res = User().check_start_time(message.from_user.id)
    if res == date.today():
        await message.answer("Удалось ли тебе связаться с куратором?",reply_markup=buttons.choice)
        await state.set_state(StartQuestion.q1)

@router.message(StartQuestion.q1)
async def start_handler2(message: Message,state:FSMContext):
    if message.text.lower() == "да":
        await message.answer('Отлично! хорошего тебе рабочего дня - вечером я еще вернусь узнать, как твои дела)')
    elif message.text.lower() == "нет":
        await state.update_data(question1=message.text)
        await state.set_state(StartQuestion.q2)
        await message.answer('Ты знаешь, кто твой куратор?')


@router.message(StartQuestion.q2)
async def start_handler2(message: Message,state:FSMContext):
    if message.text.lower() == "да":
        await message.answer('Отлично!')
    elif message.text.lower() == "нет":
        data = await state.get_data()

        await message.answer('Cейчас с тобой свяжется наш менеджер и решит проблему')
        txt = f"Работник:{message.from_user.first_name}(@{message.from_user.username}) Удалось ли тебе связаться с куратором?:{data.get('question1')}\nТы знаешь, кто твой куратор? : {Нет}"
        await bot.send_message(text.manager,txt)


    
@router.message()
async def message_handler(msg: Message):
    await send_message_to_user(msg.from_user.id, msg.text)


#yyyy
    
