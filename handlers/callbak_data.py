import asyncio
import json

from aiogram import types
from misc import dp, bot
from .sqlit import change_status,get_username
from .sqlit import reg_user, get_username,get_stat, reg_traf_support
from .sqlit import cheak_traf, get_channel_info, obnovatrafika1, delit_trafik,update_list_sub
from .generate_murkup import check_subscription,subscription_markup
import random


content = -1001819010148
reg_user(1,'1')  # Запуск в БД

text_stop = """Аяяй😝 Надо Послушать голосовой:)) а потом нажимать"""
text_stop2 = """Аяяй😝 Надо Посмотреть Видео:)) а потом нажимать."""


from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


class reg_p(StatesGroup):
    step1 = State()
    step2 = State()
    step3 = State()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message, state: FSMContext):
    channel_name = message.text[7:]

    reg_user(message.chat.id, channel_name)
    reg_traf_support(id=message.chat.id, channel=channel_name)

    if await check_subscription(message.chat.id) == True:
        update_list_sub(message.chat.id)
        await state.update_data(video1='stop')
        markup = types.InlineKeyboardMarkup()
        bat_f = types.InlineKeyboardButton(text='Нажми Как Прослушаешь гс', callback_data='sprint_online')
        markup.add(bat_f)
        await bot.copy_message(from_chat_id=content, chat_id=message.chat.id, message_id=3, reply_markup=markup)
        await asyncio.sleep(36)  # 36 секунд
        await state.update_data(video1='true')
    else:
        await bot.send_message(message.chat.id,text="""<b>⭐️ Для полноценного использования БОТА, подпишитесь на наших спонсоров:</b>""",reply_markup=subscription_markup())










@dp.callback_query_handler(lambda call: True, state = '*')
async def answer_push_inline_button(call, state: FSMContext):
    if await check_subscription(call.message.chat.id) == True:
        if call.data[0:3] == 'ch_':
            try:
                delit_trafik(call.data[3:])
                await call.message.answer("Канал успешно удален")
            except:
                await call.message.answer("Произошла ошибка")

        if call.data == 'call_check':
            if await check_subscription(call.from_user.id) == True:
                await state.update_data(video1='stop')
                markup = types.InlineKeyboardMarkup()
                bat_f = types.InlineKeyboardButton(text='Нажми Как Прослушаешь гс', callback_data='sprint_online')
                markup.add(bat_f)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=3, reply_markup=markup)
                await asyncio.sleep(36)  # 36 секунд
                await state.update_data(video1='true')
            else:
                await bot.send_message(call.message.chat.id,text="""<b>⭐️ Для полноценного использования БОТА, подпишитесь на наших спонсоров:</b>""",reply_markup=subscription_markup())

        if call.data == 'sprint_online':
            try:
                if ((await state.get_data())['video1']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_2')
                markup.add(bat_a)
                await state.update_data(video12='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=6, reply_markup=markup)
                await asyncio.sleep(180)  #180 секунд
                await state.update_data(video12='true')

        if call.data == 'new_go_1':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Погнали действовать🚀', callback_data='new_go_2')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=88)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=89,reply_markup=markup)

        if call.data == 'new_go_2':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Далее🔥', callback_data='new_go_3')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=91,reply_markup=markup)

        if call.data == 'new_go_3':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Гооо✊', callback_data='new_go_4')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=93, reply_markup=markup)

        if call.data == 'new_go_4':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='🫡 Я всё понял(а)', callback_data='new_go_5')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=95)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=96, reply_markup=markup)

        if call.data == 'new_go_5':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Далее', callback_data='new_go_6')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=98)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=99, reply_markup=markup)

        if call.data == 'new_go_6':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Далее😋', callback_data='new_go_7')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=101, reply_markup=markup)

        if call.data == 'new_go_7':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='ХОЧУ В ЧАТ😍', callback_data='new_go_8')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=103, reply_markup=markup)

        if call.data == 'new_go_8':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Я ✅ правила ', callback_data='new_go_9')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=105, reply_markup=markup)

        if call.data == 'new_go_9':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Я ✅ правила ', callback_data='new_go_9')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=107)







        if call.data == 'go_2':
            try:
                if ((await state.get_data())['video12']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop2)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Я могу 🔥', callback_data='go_31')
                bat_b = types.InlineKeyboardButton(text='Я не могу 😐', callback_data='go_32')
                markup.add(bat_a,bat_b)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=8)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=12, reply_markup=markup)

        if call.data == 'go_31':
            try:
                await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            except:
                pass

            await state.update_data(q1='yes')
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Есть 👍', callback_data='go_41')
            bat_b = types.InlineKeyboardButton(text='Нет 👎', callback_data='go_42')
            markup.add(bat_a, bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=14,reply_markup=markup)

        if call.data == 'go_32':
            try:
                await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            except:
                pass
            await state.update_data(q1='no')
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Есть 👍', callback_data='go_41')
            bat_b = types.InlineKeyboardButton(text='Нет 👎', callback_data='go_42')
            markup.add(bat_a, bat_b)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=14, reply_markup=markup)

        if call.data == 'go_41':
            try:
                await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            except:
                pass
            try:
                if ((await state.get_data())['q1']) == 'yes':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='ПОДРОБНЕЕ🧐🤩', callback_data='new_go_1')
                markup.add(bat_a)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=86,reply_markup=markup)
            else:
                await state.update_data(video2='stop')
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_5')
                markup.add(bat_a)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=22,reply_markup=markup)
                await asyncio.sleep(90)  # 90 секунд
                await state.update_data(video2='true')

        if call.data == 'go_42':
            try:
                await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
            except:
                pass
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='ПОДРОБНЕЕ🧐🤩', callback_data='new_go_1')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=86,reply_markup=markup)

        if call.data == 'go_5':
            try:
                if ((await state.get_data())['video2']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop2)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_6')
                markup.add(bat_a)

                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=25)
                await state.update_data(video3='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=26,reply_markup=markup)
                await asyncio.sleep(660)  # 11 минут (660) секунд
                await state.update_data(video3='true')

        if call.data == 'go_6':
            try:
                if ((await state.get_data())['video3']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop2)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_7')
                markup.add(bat_a)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=36)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=38)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=39)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=40,reply_markup=markup)

        if call.data == 'go_7':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_8')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=44)
            await state.update_data(video4='stop')
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=45, reply_markup=markup)
            await asyncio.sleep(90)  # 90 сек
            await state.update_data(video4='true')

        if call.data == 'go_8':
            try:
                if ((await state.get_data())['video4']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop2)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_9')
                markup.add(bat_a)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=49,reply_markup=markup)

        if call.data == 'go_9':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_10')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=52, reply_markup=markup)

        if call.data == 'go_10':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_11')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=55)
            await asyncio.sleep(10)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=57,reply_markup=markup)

        if call.data == 'go_11':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Я сделал(а)🚀', callback_data='go_12')
            markup.add(bat_a)
            await state.update_data(video5='stop')
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=59,reply_markup=markup)
            await asyncio.sleep(60)  # 60 сек
            await state.update_data(video5='true')

        if call.data == 'go_12':
            try:
                if ((await state.get_data())['video5']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop2)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Я сделал(а)🦖', callback_data='go_13')
                markup.add(bat_a)
                await state.update_data(video6='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=63,reply_markup=markup)
                await asyncio.sleep(90)  # 90 сек
                await state.update_data(video6='true')

        if call.data == 'go_13':
            try:
                if ((await state.get_data())['video6']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop2)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Я сделал(а)🎯', callback_data='go_14')
                markup.add(bat_a)

                await state.update_data(video7='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=66,reply_markup=markup)
                await asyncio.sleep(180)  # 180 сек
                await state.update_data(video7='true')

        if call.data == 'go_14':
            try:
                if ((await state.get_data())['video7']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop2)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='ДАЛЕЕ🌝', callback_data='go_15')
                markup.add(bat_a)
                await state.update_data(video8='stop')
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=70,reply_markup=markup)
                await asyncio.sleep(180)  # 180 сек
                await state.update_data(video8='true')

        if call.data == 'go_15':
            try:
                if ((await state.get_data())['video8']) == 'true':
                    flag = True
                else:
                    flag = False
            except:
                flag = True
            if flag == False:
                await bot.send_message(chat_id=call.message.chat.id, text=text_stop2)
            else:
                markup = types.InlineKeyboardMarkup()
                bat_a = types.InlineKeyboardButton(text='Хочу в Команду🙏', callback_data='go_16')
                markup.add(bat_a)
                await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=72,reply_markup=markup)

        if call.data == 'go_16':
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Далее', callback_data='go_17')
            markup.add(bat_a)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=74, reply_markup=markup)

        if call.data == 'go_17':
            change_status(call.message.chat.id)
            await bot.copy_message(from_chat_id=content, chat_id=call.message.chat.id, message_id=76)
    else:
        await bot.send_message(call.message.chat.id,
                               text="""<b>⭐️ Для полноценного использования БОТА, подпишитесь на наших спонсоров:</b>""",
                               reply_markup=subscription_markup())

    try:
        await bot.answer_callback_query(call.id)
    except:
        pass