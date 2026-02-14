from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


setting_menu_uz_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌐 Tilni o'zgartirish")],
        [KeyboardButton(text="📞 Telefon raqamingizni o'zgartiring")],
        [KeyboardButton(text="⬅️ Orqaga")]
    ],
    resize_keyboard=True
)

setting_menu_ru_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌐 Изменить язык")],
        [KeyboardButton(text="📞 Изменить номер телефона")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)

setting_menu_en_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🌐 Change language")],
        [KeyboardButton(text="📞 Change phone number")],
        [KeyboardButton(text="⬅️ Back")]
    ],
    resize_keyboard=True
)



change_lang_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text = "🇺🇿 O'zbekcha"),
            KeyboardButton(text = "🇷🇺 Русский"),
        ],
        [
            KeyboardButton(text = "🇺🇸 English")
        ],
        [
            KeyboardButton(text="⬅️ Back")
        ]
    ],
    resize_keyboard=True
)