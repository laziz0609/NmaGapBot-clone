from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext


from states.language_state import Language
from keyboards.default.settings_keyboards import (
    setting_menu_en_keyboard,
    setting_menu_ru_keyboard,
    setting_menu_uz_keyboard,
    change_lang_keyboard
)



router = Router()


@router.message(F.text == "⚙️ Sozlamalar")
async def setting_uz(message: types.Message):
    await message.answer("Sozlamalar", reply_markup=setting_menu_uz_keyboard)

@router.message(F.text == "⚙️ Настройки")
async def setting_ru(message: types.Message):
    await message.answer("Настройки", reply_markup=setting_menu_ru_keyboard)

@router.message(F.text == "⚙️ Settings")
async def setting_eng(message: types.Message):
    await message.answer("Settings", reply_markup=setting_menu_en_keyboard)


@router.message(F.text == "🌐 Tilni o'zgartirish")
async def change_lang_uz(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang", reply_markup=change_lang_keyboard)

@router.message(F.text == "🌐 Change language")
async def change_lang_uz(message: types.Message, state: FSMContext):
    await message.answer("Select a language", reply_markup=change_lang_keyboard)

@router.message(F.text == "🌐 Изменить язык")
async def change_lang_uz(message: types.Message, state: FSMContext):
    await message.answer("Выберите язык", reply_markup=change_lang_keyboard)