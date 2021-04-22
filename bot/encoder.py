from json import JSONEncoder

from bot.Message import Message


class MyEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Message):
            return {'tag': obj.tag, 'user': obj.user, 'command_text': obj.command_text,
                    'date': obj.date.strftime('%d/%m/%y %H.%M')}



