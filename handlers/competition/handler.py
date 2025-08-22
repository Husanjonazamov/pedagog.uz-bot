# start.py fayli
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from utils import texts, buttons
from asyncio.tasks import create_task



async def _task(call: CallbackQuery, state: FSMContext):
    """
     botni assosiy /start file
    """
    lang = call.from_user.language_code
    print(lang)
    
    
    await call.message.answer(
        texts.COMPETITION[lang],
        reply_markup=buttons.compotition_menu(lang)
        
    )    
    
@dp.callback_query_handler(lambda call: call.data == "competition", state="*")
async def competiton_handler(call: CallbackQuery, state: FSMContext):
    await create_task(_task(call, state))



