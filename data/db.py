import json
import aiofiles

class DB:
    def __init__(self):
        self.path = "/home/laziz/Desktop/najottalim_darslari/dars34/NmaGapBot-clone/data/users.json"


    async def add_user(self, user_id: int | str, phone_num: int | str, lang: str) -> None:
        async with aiofiles.open(self.path, "r") as file:
            content = await file.read()
            data = json.loads(content)
        data[user_id] = {"phone_num": phone_num, "lang": lang}

        async with aiofiles.open(self.path, "w") as file:
            await file.write(json.dumps(data))

    
    async def check_user(self, user_id: int | str) -> bool | dict:
        async with aiofiles.open(self.path, "r") as file:
            content = await file.read()
            data = json.loads(content)
            
            return data.get(f"{user_id}")
    
database = DB()