from . import users

# ❗ Tartib bo‘yicha: admin birinchi, user keyin
routers = [
    *users.routers,
]
