# state.py fayli
from aiogram.dispatcher.filters.state import StatesGroup, State




class ReferredState(StatesGroup):
    phone = State()
    