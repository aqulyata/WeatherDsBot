from discord import Message

from bot.command.command import Command
from bot.logic.WeatherClient import WeatherClient


class WeatherCommand(Command):

    def __init__(self):
        self.weather_client = WeatherClient()

    def weather_detailed_status(self, place):
        return self.weather_client.get_detailed_status(place)

    def weather_humidity(self, place):
        return self.weather_client.get_humidity(place)

    def weather_temperature(self, place):
        return self.weather_client.get_temperature(place)

    async def execute(self, msg: Message):
        city = msg.content.split()[1]
        await msg.channel.send(f'Погода сегодня:\nСтатус: {self.weather_detailed_status(city)}\n'
                               f'Влажность: {self.weather_humidity(city)}%\n'
                               f'Температура в районе: {self.weather_temperature(city)} градусов цельсия')

    def get_name(self):
        return 'weather'
