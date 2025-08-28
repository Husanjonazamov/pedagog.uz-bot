# start.py fayli
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from asyncio.tasks import create_task
from state.state import ReferredState

from services.services import TopListUser




async def _task(message: Message, state: FSMContext):
    """
    Reff handler
    """
    
    print("salom")
    
    tg_id = message.from_user.id
    lang = message.from_user.language_code
    data = TopListUser()
    
    text = texts.TOP_LIST_HEADER[lang] + "\n\n"
    
    for index, user in enumerate(data, start=1):
        count = user['referral_count']
        first_name = user.get('first_name') or ""
        last_name = user.get('last_name') or ""
        full_name = f"{first_name} {last_name}".strip()

        text += f"{index}. {full_name} - {count}\n"
        
        
    await message.answer(
        text
    )


@dp.message_handler(lambda message: message.text in (
    buttons.top_referrals_uz,
    buttons.top_referrals_ru,
    buttons.top_referrals_en,
), state="*")
async def topref_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))



