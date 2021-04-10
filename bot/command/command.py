from discord import Message


class Command:
    async def execute(self, msg: Message):
        ...

    def get_name(self):
        ...
