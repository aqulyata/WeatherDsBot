import json

import discord
from discord import utils
import config
from bot.Message import Message
from bot.command.command import Command
#from bot.command.mention import MentionCommand
from bot.command.weather import WeatherCommand
from bot.logic.JsonManager import JsonManager

prefix = '!'


class WeatherBotClient(discord.Client):

    def __init__(self):
        super().__init__()
        self.commands = {}
        self.json_manager: JsonManager = JsonManager()
        

    async def on_ready(self):
        print('Logged on as', self.user)
        with open('users_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            print(data)

    async def on_message(self, message):

        split_message = message.content.split()

        tag = split_message[0]

        if message.author == self.user:
            start_author = self.user
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

    async def on_raw_reaction_add(self, payload):
            channel = self.get_channel(payload.channel_id)  # get channel object
            msg = await channel.fetch_message(payload.message_id)  # get the message object
            member = utils.get(msg.guild.members)
            if member.id != payload.user_id:
                await msg.add_reaction("⏰")


                print(payload.user_id)
                emoji = str(payload.emoji)
                print(emoji)

    # async def on_raw_reaction_remove(self, payload):
    #     channel = self.get_channel(payload.channel_id)  # get channel object
    #     msg = await channel.fetch_message(payload.message_id)  # get the message object
    #     member = utils.get(msg.guild.members)  # get the user object who set the reaction
    #     if member.id != payload.user_id:
    #         None






            #async def on_raw_reaction_add(self, payload):
        #if payload.message_id == config.POST_ID:
            #channel = self.get_channel(payload.channel_id) # получаем объект канала
            # = await channel.fetch_message(payload.message_id) # получаем объект сообщения
            #member = utils.get(message.guild.members, id=payload.user_id)

    def register_command(self, command: Command):
        self.commands[command.get_name()] = command


bot = WeatherBotClient()

bot.register_command(WeatherCommand())

#bot.register_command(MentionCommand())

bot.run(config.token)
