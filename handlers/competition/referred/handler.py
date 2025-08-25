# start.py fayli
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from asyncio.tasks import create_task
from state.state import ReferredState

from services.services import check_user




async def _task(message: Message, state: FSMContext):
    """
    Reff handler
    """
    
    print("salom")
    
    tg_id = message.from_user.id
    lang = message.from_user.language_code
    data = check_user(tg_id)

    if data and "referral_link" in data:
        ref_link = data['referral_link']
        print(ref_link)
        await message.answer(
            texts.REF_LINK[lang].format(ref_link),
            reply_markup=buttons.referral_buttons(ref_link=ref_link, lang=lang)
        )
    else:
        await message.answer(
            texts.REF_PHONE[lang],
            reply_markup=buttons.ref_phone(lang)
        )    
        await ReferredState.phone.set()
    
    
@dp.message_handler(lambda message: message.text in (
    buttons.referral_uz,
    buttons.referral_en,
    buttons.referral_ru,
), state="*")
async def ref_handler(message: Message, state: FSMContext):
    await create_task(_task(message, state))



