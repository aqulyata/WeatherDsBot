from discord import Message
from pyowm import OWM

from bot.command.command import Command


class WeatherCommand(Command):

    def weather_detailed_status(self, place):
        owm = OWM("0daf1e3463914472f26d510ae197bd02")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        det = w.detailed_status
        return det

    def weather_humidity(self, place):
        owm = OWM("0daf1e3463914472f26d510ae197bd02")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        hum = w.humidity
        return hum

    def weather_temperature(self, place):
        owm = OWM("0daf1e3463914472f26d510ae197bd02")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        tem = w.temperature('celsius')["temp"]
        return tem

    async def execute(self, msg: Message):
        city = msg.content.split()[1]
        await msg.channel.send(f'Погода сегодня:\nОблачность: {self.weather_detailed_status(city)}\n'
                               f'Влажность: {self.weather_humidity(city)}\n'
                               f'Температура в районе: {self.weather_temperature(city)} градусов цельсия')

    def get_name(self):
        return 'weather'
