import json
import aiofiles

class DB:
    def __init__(self):
        self.path = "/home/laziz/Desktop/najottalim_darslari/dars34/NmaGapBot-clone/data/users.json"


    async def add_user(self, user_id: int | str, phone_num: int | str) -> None:
        async with aiofiles.open(self.path, "r") as file:
            content = await file.read()
            data = json.loads(content)

        print(type(user_id))
        print(user_id)
        print(data)
        data[user_id] = phone_num

        async with aiofiles.open(self.path, "w") as file:
            await file.write(json.dumps(data))


    
    async def check_user(self, user_id: int | str) -> bool:
        async def add_user(self, user: dict) -> None:
            async with aiofiles.open(self.path, "r") as file:
                content = file.read()
                data = json.load(content)

            return data.get(user_id) != None
        
database = DB()