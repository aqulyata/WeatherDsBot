import discord

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

from bot.command.command import Command
from bot.logic.WeatherClient import WeatherClient

config_dict = get_default_config()
config_dict['language'] = 'ru'
owm = OWM("0daf1e3463914472f26d510ae197bd02", config_dict)



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
        city = msg.content.split()[1]
        emb = discord.Embed(title="Погода", description=(
            f'Cправочное время: {self.weather_reference("iso")}:\nОблачность: {self.weather_detailed_status(city)}\nДавление: {self.weather_pressure(city)} мм.рт.ст'
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
                city) == "небольшой дождь":
            emb.set_image(url="https://image.flaticon.com/icons/png/128/1779/1779940.png")  # rain
        elif self.weather_detailed_status(city) == "небольшой снег" or self.weather_detailed_status(city) == "снег":
            emb.set_image(
                url='https://t4.ftcdn.net/jpg/03/96/45/43/240_F_396454372_WsYRTprEjwLRSoacG9LuB7ZPXdCN5fDR.jpg')
        elif self.weather_detailed_status(city) == "плотный туман" or self.weather_detailed_status(city) == "туман":
            emb.set_image(url='https://image.flaticon.com/icons/png/128/1057/1057840.png')

        await msg.channel.send(embed=emb)

    def get_name(self):
        return 'weather'
