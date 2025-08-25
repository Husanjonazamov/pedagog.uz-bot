# start.py fayli
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from asyncio.tasks import create_task




async def _task(message: Message, state: FSMContext):
    """
     botni assosiy /start file
    """
    lang = message.from_user.language_code
    text = texts.START[lang]
    user_id = message.from_user.id
    
    buttons.send_webapp_button(lang=lang, user_id=user_id, text=text)
    
    
@dp.message_handler(commands=['start'], state="*")
async def start_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))



