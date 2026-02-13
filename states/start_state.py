from aiogram.fsm.state import State, StatesGroup

class StartState(StatesGroup):
    choice_lang = State()
    send_num = State()