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
    
    await message.answer(
        texts.HELP 
    )
        
    
    
@dp.message_handler(commands=['help'], state="*")
async def help_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))



