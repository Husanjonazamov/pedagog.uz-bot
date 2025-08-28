# start.py fayli
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from asyncio.tasks import create_task
from state.state import ReferredState

from services.services import getUserPoints



async def _task(message: Message, state: FSMContext):
    """
    Reff handler
    """
    
    print("salom")

    tg_id = message.from_user.id
    lang = message.from_user.language_code
    data = getUserPoints(tg_id)
    
    await message.answer(
        texts.GIFTS[lang].format(ref_link="https://t.me/Pedagog_uzbot")
    )
    

@dp.message_handler(lambda message: message.text in (
    buttons.gifts_uz,
    buttons.gifts_en,
    buttons.gifts_ru,
), state="*")
async def points_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))



