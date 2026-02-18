from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo


main_menu_uz = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🛍 Buyurtma berish", web_app=WebAppInfo(url="https://uzum.uz/uz")
            )
        ],
        [
            KeyboardButton(text="📦 Buyurtmalarim"),
            KeyboardButton(
                text="⚙️ Sozlamalar",
            ),
        ],
        [
            KeyboardButton(text="ℹ️ Biz haqimizda"),
            KeyboardButton(text="✍️ Fikr qoldirish"),
        ],
    ],
    resize_keyboard=True,
)

main_menu_ru = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🛍 Сделать заказ", web_app=WebAppInfo(url="https://uzum.uz/ru")
            )
        ],
        [KeyboardButton(text="📦 Мои заказы"), KeyboardButton(text="⚙️ Настройки")],
        [KeyboardButton(text="ℹ️ О нас"), KeyboardButton(text="✍️ Оставить отзыв")],
    ],
    resize_keyboard=True,
)

main_menu_en = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🛍 Place an order", web_app=WebAppInfo(url="https://uzum.uz")
            )
        ],
        [KeyboardButton(text="📦 My orders"), KeyboardButton(text="⚙️ Settings")],
        [KeyboardButton(text="ℹ️ About us"), KeyboardButton(text="✍️ Leave feedback")],
    ],
    resize_keyboard=True,
)


texts = {
    "uz": {
        "text": "Tilni tanlang",
        "main_menu": [
            "🛍 Buyurtma berish",
            "📦 Buyurtmalarim",
            "ℹ️ Biz haqimizda",
            "⚙️ Sozlamalar",
            "✍️ Fikr qoldirish",
        ],
        "settings_menu": [
            "🌐 Tilni o'zgartirish",
            "📞 Telefon raqamingizni o'zgartiring",
        ],
        "back": "⬅️ Orqaga",
    },
    "ru": {
        "text": "Выберите язык",
        "main_menu": [
            "🛍 Сделать заказ",
            "📦 Мои заказы",
            "ℹ️ О нас",
            "⚙️ Настройки",
            "✍️ Оставить отзыв",
        ],
        "settings_menu": ["🌐 Изменить язык", "📞 Изменить номер телефона"],
        "back": "⬅️ Назад",
    },
    "en": {
        "text": "Select language",
        "main_menu": [
            "🛍 Place an order",
            "📦 My orders",
            "ℹ️ About us",
            "⚙️ Settings",
            "✍️ Leave feedback",
        ],
        "settings_menu": ["🌐 Change language", "📞 Change phone number"],
        "back": "⬅️ Back",
    },
}
