from aiogram import types
from misc import dp,bot
import asyncio

ADMIN_ID_1 = 494588959 #Cаня
ADMIN_ID_2 = 44520977 #Коля
ADMIN_ID = [ADMIN_ID_1,ADMIN_ID_2]

flag1 = 1 #НАСТРОЙКА РЕЖИМА ПОКАЗА FILE ID

@dp.message_handler(content_types=['text', 'photo', 'video_note', 'animation', 'document', 'video','file'])
async def all_message(message: types.Message):
    try:
        print(message.video.file_id)
    except:
        pass

    try:
        print(message.photo[0].file_id)
    except:
        pass

    try:
        print(message.video_note.file_id)
    except:
        pass

    try:
        print(message.animation.file_id)
    except:
        pass

    try:
        print(message.document.file_id)
    except:
        pass