from aiogram import types, Router, F


router = Router()


@router.message(F.text == "📦 Buyurtmalarim")
async def orders_uz(message: types.Message):
    await message.answer("Sizda hali birorta ham buyurtma yo'q")


@router.message(F.text == "📦 Мои заказы")
async def orders_ru(message: types.Message):
    await message.answer("У вас пока нет ни одного заказа.")


@router.message(F.text == "📦 My orders")
async def orders_eng(message: types.Message):
    await message.answer("You don’t have any orders yet.")


@router.message(F.text == "ℹ️ Biz haqimizda")
async def info_uz(message: types.Message):
    await message.answer(
        "Shu yerda joylashganmiz.\nElektron pochta: abror4work@gmail.com"
    )


@router.message(F.text == "ℹ️ О нас")
async def info_ru(message: types.Message):
    await message.answer("Мы находимся здесь.\nЭлектронная почта: abror4work@gmail.com")


@router.message(F.text == "ℹ️ About us")
async def info_eng(message: types.Message):
    await message.answer("We are located here.\nEmail: abror4work@gmail.com")
