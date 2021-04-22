import discord

import config
from bot.command.command import Command
from bot.command.weather import WeatherCommand
from bot.logic.JsonManager import JsonManager
from bot.Message import Message

prefix = '!'


class WeatherBotClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.commands = {}
        self.json_manager: JsonManager = JsonManager()

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):

        split_message = message.content.split()

        tag = split_message[0]

        if message.author == self.user:
            return

        text = message.content

        if not text.startswith(prefix):
            return

        text = text[len(prefix):]

        cmd = text.split()[0]

        if cmd not in self.commands:
            return

        self.json_manager.add_message(Message(tag, message.author, message.content))

        await self.commands[cmd].execute(message)

    def register_command(self, command: Command):
        self.commands[command.get_name()] = command


bot = WeatherBotClient()

bot.register_command(WeatherCommand())

bot.run(config.token)
