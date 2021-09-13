import discord
from discord import utils
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

# from bot.main import bot
from bot.command.command import Command
from bot.logic.WeatherClient import WeatherClient

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM("9fc48cdda1363903e05d3c37dc39b6a8", config_dict)
a = 1


#bot=discord.command.Bot

class WeatherCommand(Command):

    def __init__(self):
        self.weather_client = WeatherClient()

    def weather_reference(self, place):
        return self.weather_client.get_reference(place)

    def weather_pressure(self, place):
        return self.weather_client.get_pressure(place)

    def weather_detailed_status(self, place):
        return self.weather_client.get_detailed_status(place)

    def weather_humidity(self, place):
        return self.weather_client.get_humidity(place)

    def weather_temperature(self, place):
        return self.weather_client.get_temperature(place)

    async def execute(self, msg: discord.Message):

        author = msg.author
        id = author.id
        city = msg.content.split()[1]
        emb = discord.Embed(title="Погода", description=(
            f'<@{id}>\nCправочное время: {self.weather_reference("iso")}:\nОблачность: {self.weather_detailed_status(city)}\nДавление: {self.weather_pressure(city)} мм.рт.ст'
            f'\nТемпература в районе: {self.weather_temperature(city)} градусов цельсия'),
                            colour=discord.Color.green())
        if self.weather_detailed_status(city) == "небольшая облачность" or self.weather_detailed_status(
                city) == "few clouds" or self.weather_detailed_status(
            city) == "переменная облачность" or self.weather_detailed_status(city) == 'broken clouds':
            emb.set_image(url="https://image.flaticon.com/icons/png/128/1146/1146869.png")  # scattered clouds
        elif self.weather_detailed_status(city) == "ясно":
            if self.weather_temperature(city) > -5:
                emb.set_image(url="https://image.flaticon.com/icons/png/128/869/869869.png")  # sun
            else:
                emb.set_image(url="https://image.flaticon.com/icons/png/128/2938/2938130.png")
        elif self.weather_detailed_status(city) == "пасмурно" or self.weather_detailed_status(
                city) == "небольшой дождь" or self.weather_detailed_status(city) == "проливной дождь":
            await msg.channel.send(f"https://yandex.ru/pogoda/{city}/maps/nowcast?via=hnav&le_Lightning=1")
            emb.set_image(url="https://image.flaticon.com/icons/png/128/1779/1779940.png")  # rain
        elif self.weather_detailed_status(city) == "небольшой снег" or self.weather_detailed_status(city) == "снег":
            emb.set_image(
                url='https://t4.ftcdn.net/jpg/03/96/45/43/240_F_396454372_WsYRTprEjwLRSoacG9LuB7ZPXdCN5fDR.jpg')
        elif self.weather_detailed_status(city) == "плотный туман" or self.weather_detailed_status(city) == "туман":
            emb.set_image(url='https://image.flaticon.com/icons/png/128/1057/1057840.png')

        msg = await msg.channel.send(embed=emb)
        message_id=msg.id
        await msg.add_reaction('✅')
        reaction = '✅'

        async def on_raw_reaction_add(self, payload):
            if payload.message_id == message_id:
                channel = self.get_channel(payload.channel_id)  # get channel object
                message = await channel.fetch_message(payload.message_id)  # get the message object
                member = utils.get(message.guild.members, id=payload.user_id)
                print(member)
        # for reaction in resactions:
        #     result += reaction.emoji + ": " + str(reaction.count - 1)
        # if reaction.count<0:
        #     print("good")
        #page = Paginator(bot, msg, only=msg.author, use_more=False)
        #await page.start()

    def get_name(self):
        return 'weather'
