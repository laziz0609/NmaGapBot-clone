from aiogram.fsm.state import State, StatesGroup

class Language(StatesGroup):
    uz = State()
    ru = State()
    eng = State()