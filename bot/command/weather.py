import discord
from pyowm import OWM
from pyowm.utils.config import get_default_config
from bot.command.command import Command
config_dict=get_default_config()
config_dict["language"] = "ru"

class WeatherCommand(Command):

    def weather_detailed_status(self, place):
        owm = OWM("0daf1e3463914472f26d510ae197bd02")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        det = w.detailed_status
        config_dict=get_default_config()
        config_dict["language"] = "ru"
        return det

    def weather_pressure(self, place):
        owm = OWM("0daf1e3463914472f26d510ae197bd02")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        press= w.pressure["press"]
        return press

    def weather_temperature(self, place):
        owm = OWM("0daf1e3463914472f26d510ae197bd02")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        tem = w.temperature('celsius')["temp"]
        return tem

    def weather_reference(self, place):
        owm = OWM("0daf1e3463914472f26d510ae197bd02")
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(place)
        w = observation.weather
        time = w.reference_time("iso")
        return time

    async def execute(self, msg: discord.Message):
        city = msg.content.split()[1]
        emb = discord.Embed(title="Погода", description=(
            f'Cправочное время: {self.weather_reference("iso")}:\nОблачность: {self.weather_detailed_status(city)}\nДавление: {self.weather_pressure(city)} мм.рт.ст'
            f'\nТемпература в районе: {self.weather_temperature(city)} градусов цельсия'),
                            colour=discord.Color.green())
        if self.weather_detailed_status(city) == "небольшая облачность" or self.weather_detailed_status(city) == "few clouds" or self.weather_detailed_status(city) == "переменная облачность" or self.weather_detailed_status(city) =='broken clouds':
            emb.set_image(url="https://image.flaticon.com/icons/png/128/1146/1146869.png")  # scattered clouds
        elif self.weather_detailed_status(city) == "ясно":
            if self.weather_temperature(city) > -5:
                emb.set_image(url="https://image.flaticon.com/icons/png/128/869/869869.png")  # sun
            else:
                emb.set_image(url="https://image.flaticon.com/icons/png/128/2938/2938130.png")
        elif self.weather_detailed_status(city) == "пасмурно" or self.weather_detailed_status(city) == "небольшой дождь":
            emb.set_image(url="https://image.flaticon.com/icons/png/128/1779/1779940.png")  # rain
        elif self.weather_detailed_status(city) == "небольшой снег" or self.weather_detailed_status(city) == "снег":
            emb.set_image(url='https://t4.ftcdn.net/jpg/03/96/45/43/240_F_396454372_WsYRTprEjwLRSoacG9LuB7ZPXdCN5fDR.jpg')
        elif self.weather_detailed_status(city) == "плотный туман" or self.weather_detailed_status(city) == "туман":
            emb.set_image(url='https://image.flaticon.com/icons/png/128/1057/1057840.png')

        await msg.channel.send(embed=emb)

    def get_name(self):
        return 'weather'
