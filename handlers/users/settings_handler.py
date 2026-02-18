from aiogram import types, Router, F
from aiogram.fsm.context import FSMContext


from data import database
from states.language_state import Language, Change_language, ChangNum
from keyboards.default.settings_keyboards import (
    setting_menu_en_keyboard,
    setting_menu_ru_keyboard,
    setting_menu_uz_keyboard,
    change_lang_keyboard,
    change_phone_num_eng,
    change_phone_num_ru,
    change_phone_num_uz,
)
from keyboards.default.menu_keyboards import (
    main_menu_en,
    main_menu_ru,
    main_menu_uz
)



router = Router()

# sozlamalarga kirish
@router.message(F.text == "⚙️ Sozlamalar")
async def setting_uz(message: types.Message):
    await message.answer("Sozlamalar", reply_markup=setting_menu_uz_keyboard)


@router.message(F.text == "⚙️ Настройки")
async def setting_ru(message: types.Message):
    await message.answer("Настройки", reply_markup=setting_menu_ru_keyboard)


@router.message(F.text == "⚙️ Settings")
async def setting_eng(message: types.Message):
    await message.answer("Settings", reply_markup=setting_menu_en_keyboard)


# bosh sahifaga qaytish
@router.message(F.text == "⬅️ Orqaga")
async def back_main_menu_uz(message: types.Message, state: FSMContext):
    await message.answer("Bosh sahifa", reply_markup=main_menu_uz)
    await state.set_state(Language.uz)

@router.message(F.text == "⬅️ Назад")
async def back_main_menu_ru(message: types.Message, state: FSMContext):
    await message.answer("Главная страница", reply_markup=main_menu_ru)
    await state.set_state(Language.ru)

@router.message(F.text == "⬅️ Back")
async def back_main_menu_eng(message: types.Message, state: FSMContext):
    await message.answer("Home page", reply_markup=main_menu_en)
    await state.set_state(Language.eng)


# tilni o'zgartirish
@router.message(F.text == "🌐 Tilni o'zgartirish")
async def change_lang_uz(message: types.Message, state: FSMContext):
    await message.answer("Tilni tanlang", reply_markup=change_lang_keyboard)
    await state.set_state(Change_language.chang_lang)

@router.message(F.text == "🌐 Change language")
async def change_lang_eng(message: types.Message, state: FSMContext):
    await message.answer("Select a language", reply_markup=change_lang_keyboard)
    await state.set_state(Change_language.chang_lang)

@router.message(F.text == "🌐 Изменить язык")
async def change_lang_ru(message: types.Message, state: FSMContext):
    await message.answer("Выберите язык", reply_markup=change_lang_keyboard)
    await state.set_state(Change_language.chang_lang)

@router.message(F.text, Change_language.chang_lang)
async def select_lang(message: types.Message, state: FSMContext):
    if message.text == "🇺🇿 O'zbekcha":
        await message.answer("Bosh menu", reply_markup=main_menu_uz)
        await state.set_state(Language.uz)
        await database.change_user_lang(message.from_user.id, "uz")
    
    elif message.text == "🇷🇺 Русский":
        await message.answer("Главная страница", reply_markup=main_menu_ru)
        await state.set_state(Language.ru)
        await database.change_user_lang(message.from_user.id, "ru")

    elif message.text == "🇺🇸 English":
        await message.answer("Home page", reply_markup=main_menu_en)
        await state.set_state(Language.eng)
        await database.change_user_lang(message.from_user.id, "eng")


# raqamni o'zgartirish
@router.message(F.text == "📞 Telefon raqamini o'zgartirish")
async def change_phone_number_uz(message: types.Message, state: FSMContext):
    await message.answer("Raqamingizni kiriting", reply_markup=change_phone_num_uz)
    await state.set_state(ChangNum.phone_num)

@router.message(F.text == "📞 Изменить номер телефона")
async def change_phone_number_ru(message: types.Message, state: FSMContext):
    await message.answer("Введите свой номер", reply_markup=change_phone_num_ru)
    await state.set_state(ChangNum.phone_num)

@router.message(F.text == "📞 Change phone number")
async def change_phone_number_eng(message: types.Message, state: FSMContext):
    await message.answer("Enter your number", reply_markup=change_phone_num_eng)
    await state.set_state(ChangNum.phone_num)

@router.message(F.contact, ChangNum.phone_num)
async def change_contact(message: types.Message, state: FSMContext):
    if message.contact.user_id != message.from_user.id:
        return 
    
    user_info = await database.check_user(message.from_user.id)
    if not user_info:
        await message.answer("Error   /start")
        return
    
    await database.change_user_phone_num(message.from_user.id, message.contact.phone_number)

    lang = user_info["lang"]

    if lang == "uz":
        await message.answer("Telefon raqam o'zgartirildi", reply_markup=main_menu_uz)
        await state.set_state(Language.uz)

    elif lang == "ru":
        await message.answer("Номер телефона изменен", reply_markup=main_menu_ru)
        await state.set_state(Language.ru)

    elif lang == "eng":
        await message.answer("Phone number changed", reply_markup=main_menu_en)
        await state.set_state(Language.eng)



    
    


    






