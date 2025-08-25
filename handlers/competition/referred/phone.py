from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import texts, buttons
from asyncio.tasks import create_task
from state.state import ReferredState
from services.services import check_phone



def normalize_phone(phone: str) -> str:
    """Telefon raqamini 998 bilan boshlanadigan formatga keltiradi"""
    phone = phone.replace("+", "").strip()
    if not phone.startswith("998"):
        if phone.startswith("8"):  
            phone = "998" + phone[1:]
        elif len(phone) == 9:  
            phone = "998" + phone
    return phone





async def _task(message: Message, state: FSMContext):
    lang = message.from_user.language_code or "uz"
    phone = None

    if message.contact:
        phone = message.contact.phone_number
    elif message.text:
        if message.text.isdigit() and len(message.text) >= 9:
            phone = message.text
        else:
            await message.answer(texts.REF_PHONE_INVALID[lang])
            return

    if not phone:
        await message.answer(texts.REF_PHONE_ERROR[lang])
        return

    phone = normalize_phone(phone)

    user_data = {
        "tg_id": message.from_user.id,
        "phone": int(phone)
    }
    print(user_data)

    data = check_phone(user_data)
    print("API response:", data)

    if data.get("exists") and data.get("referral_link"):
        referral_link = data['referral_link']
        await message.answer(
            texts.REF_LINK[lang].format(referral_link),
            reply_markup=buttons.referral_buttons(lang=lang, ref_link=referral_link)
        )
    else:
        await message.answer(texts.REF_PHONE_NOT_FOUND[lang])

    await state.finish()



@dp.message_handler(content_types=['contact', 'text'], state=ReferredState.phone)
async def ref_phone(message: Message, state: FSMContext):
    await create_task(_task(message, state))
