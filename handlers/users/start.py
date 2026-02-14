from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext



from data import database
from states import StartState, Language
from keyboards.default.start_keybords import (
    choice_lang, 
    send_phone_num_eng,
    send_phone_num_ru,
    send_phone_num_uz

)
from keyboards.default.menu_keyboards import (
    main_menu_en,
    main_menu_ru,
    main_menu_uz
)



router = Router()


@router.message(Command("start"), Language.uz)
async def start_uz(message: types.Message, state: FSMContext):
    await message.answer(f"Salom <b>{message.from_user.first_name}</b>", reply_markup=main_menu_uz, parse_mode="html")

@router.message(Command("start"), Language.ru)
async def start_uz(message: types.Message, state: FSMContext):
    await message.answer(f"Привет <b>{message.from_user.first_name}</b>", reply_markup=main_menu_ru, parse_mode="html")

@router.message(Command("start"), Language.eng)
async def start_uz(message: types.Message, state: FSMContext):
    await message.answer(f"Hello <b>{message.from_user.first_name}</b>", reply_markup=main_menu_en, parse_mode="html")


@router.message(Command("start"))
async def start(message: types.Message, state: FSMContext):
    check_user = await database.check_user(message.from_user.id)
    if check_user:
        if check_user.get("lang"):
            lang = check_user["lang"]

            if lang == "uz":
                await state.set_state(Language.uz)
                await message.answer(f"Salom ,<b>{message.from_user.first_name}</b>", reply_markup=main_menu_uz, parse_mode="html")
            
            elif lang == "ru":
                await state.set_state(Language.ru)
                await message.answer(f"Привет ,<b>{message.from_user.first_name}</b>", reply_markup=main_menu_ru, parse_mode="html")

            elif lang == "eng":
                await state.set_state(Language.eng)
                await message.answer(f"Hello ,<b>{message.from_user.first_name}</b>", reply_markup=main_menu_en, parse_mode="html")

            return
        
    await message.answer("Iltimos tilni tanlang", reply_markup=choice_lang)
    await state.set_state(StartState.choice_lang)


@router.message(F.text, StartState.choice_lang)
async def choice_lang_handler(message: types.Message, state: FSMContext):
    if message.text == "🇺🇿 O'zbekcha":
        await state.set_state(StartState.send_num)
        await state.update_data(lang = "uz")
        await message.answer("📞 Raqamingizni kiriting", reply_markup=send_phone_num_uz)
    
    elif message.text == "🇷🇺 Русский":
        await state.set_state(StartState.send_num)
        await state.update_data(lang = "ru")
        await message.answer("📞 Введите ваш номер телефона", reply_markup=send_phone_num_ru)

    elif message.text == "🇺🇸 English":
        await state.set_state(StartState.send_num)
        await state.update_data(lang = "eng")
        await message.answer("📞 Enter your phone number", reply_markup=send_phone_num_eng)

    else:
        await message.answer("Iltimos tilni tanlang")


@router.message(F.contact, StartState.send_num)
async def send_num_handler(message: types.Message, state: FSMContext):
    contact = message.contact
    data = await state.get_data()
    lang = data["lang"]
    
    if  contact.user_id != message.from_user.id:
        if lang == "uz":
            await message.answer("📞 Iltimos, telefon raqamingizni yuboring")
        
        elif lang == "ru":
            await message.answer("📞 Пожалуйста, отправьте ваш номер телефона")

        elif lang == "eng":
            await message.answer("📞 Please send your phone number")

        return
    

    user_id = message.from_user.id
    phone_num = contact.phone_number 

    await database.add_user(user_id=user_id, phone_num=phone_num, lang=lang)
    await state.clear()

    if lang == "uz":
        await message.answer("✅ Raqamingiz saqlandi", reply_markup=main_menu_uz) 
        await state.set_state(Language.uz)
    elif lang == "ru":
        await message.answer("✅ Ваш номер сохранён", reply_markup=main_menu_ru) 
        await state.set_state(Language.ru)
    elif lang == "eng":
        await message.answer("✅ Your phone number has been saved", reply_markup=main_menu_en) 
        await state.set_state(Language.eng)
