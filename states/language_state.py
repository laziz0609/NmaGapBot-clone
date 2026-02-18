from aiogram.fsm.state import State, StatesGroup


class Language(StatesGroup):
    uz = State()
    ru = State()
    eng = State()


class Change_language(StatesGroup):
    chang_lang = State()

class ChangNum(StatesGroup):
    phone_num = State()
