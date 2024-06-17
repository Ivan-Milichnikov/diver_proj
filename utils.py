import json
from aiogram import Bot

def send_message_to_user(user_id, message):
    try:
        bot.send_message(chat_id=user_id, text=message)
        print(f"Сообщение отправлено пользователю с ID {user_id}")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {e}")


bot = Bot(token="2047427917:AAHqiDbjHn08s8EdkPWuz4wbLJjjY_vf4mY")