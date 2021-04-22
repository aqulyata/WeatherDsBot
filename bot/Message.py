import datetime


class Message:

    def __init__(self, tag, user, command_text):
        self.tag = tag
        self.user = user.display_name
        self.date = datetime.datetime.now()
        self.command_text = command_text
