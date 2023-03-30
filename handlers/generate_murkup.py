from aiogram import types
from .sqlit import get_channel_info
from aiogram import types
from misc import dp,bot

def subscription_markup():
    markup = types.InlineKeyboardMarkup()
    data = get_channel_info()
    for d in data:
        markup.add(types.InlineKeyboardButton(text=d[0], url = d[1]))
    markup.add(types.InlineKeyboardButton(text='🥤Я ПОДПИСАЛСЯ🥤', callback_data=f'call_check'))
    return markup


async def check_subscription(user_id):
    data = get_channel_info()
    flag = 1

    for d in data:
        try:
            proverka = (await bot.get_chat_member(chat_id=d[2], user_id=user_id)).status
        except:
            proverka = 'member'


        if proverka == 'member' or proverka == 'administrator' or proverka == 'creator':
            pass
        else:
            flag = 0

    if flag == 1:  # Человек прошел все 3 проверки
        return True
    else:
        return False