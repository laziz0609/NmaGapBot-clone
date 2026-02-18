import json
import aiofiles


class DB:
    def __init__(self):
        self.path = "/home/laziz/Desktop/najottalim_darslari/dars34/NmaGapBot-clone/data/users.json"

    async def add_user(
        self, user_id: int, phone_num: int | str, lang: str
    ) -> None:
        async with aiofiles.open(self.path, "r") as file:
            content = await file.read()
            data = json.loads(content)
        data[user_id] = {"phone_num": phone_num, "lang": lang}

        async with aiofiles.open(self.path, "w") as file:
            await file.write(json.dumps(data))


    async def check_user(self, user_id: int) -> bool | dict:
        async with aiofiles.open(self.path, "r") as file:
            content = await file.read()
            data = json.loads(content)

            return data.get(f"{user_id}")
        
    
    async def change_user_lang(self, user_id: int, lang: str) -> None:
        async with aiofiles.open(self.path, "r") as file:
            content = await file.read()
            data = json.loads(content)

            data[str(user_id)]["lang"] = lang

        async with aiofiles.open(self.path, "w") as file:
            await file.write(json.dumps(data))


    async def change_user_phone_num(self, user_id: int, phone_num: str | int) -> None:
        async with aiofiles.open(self.path, "r") as file:
            content = await file.read()
            data = json.loads(content)

            data[str(user_id)]["phone_num"] = phone_num

        async with aiofiles.open(self.path, "w") as file:
            await file.write(json.dumps(data))

database = DB()
