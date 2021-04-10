import discord

from bot.command.command import Command
from bot.command.weather import WeatherCommand
from config import token

prefix = '!'


class WeatherBotClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.commands = {}

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, msg: discord.Message):

        if msg.author == self.user:
            return

        text = msg.content

        if not text.startswith(prefix):
            return

        text = text[len(prefix):]

        cmd = text.split()[0]

        if cmd not in self.commands:
            return

        await self.commands[cmd].execute(msg)

    def register_command(self, command: Command):
        self.commands[command.get_name()] = command


bot = WeatherBotClient()

bot.register_command(WeatherCommand())

bot.run(token)
