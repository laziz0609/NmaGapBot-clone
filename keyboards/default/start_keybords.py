from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choice_lang = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🇺🇿 O'zbekcha"),
            KeyboardButton(text="🇷🇺 Русский"),
        ],
        [KeyboardButton(text="🇺🇸 English")],
    ],
    resize_keyboard=True,
)


send_phone_num_eng = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📞 Send phone number", request_contact=True)]],
    resize_keyboard=True,
)

send_phone_num_ru = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📞 Отправить номер", request_contact=True)]],
    resize_keyboard=True,
)

send_phone_num_uz = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="📞 Raqamni yuborish", request_contact=True)]],
    resize_keyboard=True,
)
