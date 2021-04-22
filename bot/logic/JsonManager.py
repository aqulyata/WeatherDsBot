from bot.encoder import MyEncoder
from bot.Message import Message
import json


class JsonManager:
    BLOCK_SIZE = 10

    def __init__(self):
        self.messages: [Message] = []

    def add_message(self, message: Message):
        self.messages.append(message)
        if len(self.messages) % JsonManager.BLOCK_SIZE == 0:
            self.write_to_file()

    def write_to_file(self):
        print(f'write to file {len(self.messages)}')
        with open('users_data.json', 'w', encoding='utf-8') as file:
            json.dump(self.messages, file, cls=MyEncoder, indent=4, ensure_ascii=False)

    def destruct(self):
        ...


    #todo 1 считывать файл при старте
    #todo 2 в деструкторе дописать все что не влезло в блок