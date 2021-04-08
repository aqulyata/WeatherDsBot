import json

from pyowm import OWM
import discord
from discord.ext import commands
from config import token
client = discord.Client()
#gg

data={
        "type": "search by Artist",
        "artist": "Артур Пирожков",
        "user": "Forichok",
        "date": "2021-03-05T19:19:48Z"
}

with open("my.json", "w") as file:
    json.dump(data, file, indent=3)

def opening():
    with open("my.json", "r") as file:
        data = json.load(file)
        return data

def weatherDet(place):
    owm = OWM("0daf1e3463914472f26d510ae197bd02")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    det = w.detailed_status
    return det
def weatherHum(place):
    owm = OWM("0daf1e3463914472f26d510ae197bd02")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    hum=w.humidity
    return hum


def weatherTem(place):
    owm = OWM("0daf1e3463914472f26d510ae197bd02")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(place)
    w = observation.weather
    tem=w.temperature('celsius')["temp"]
    return tem


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message: discord.Message):

    if message.author == client.user:
        return

    if message.content.startswith('!weather'):
        city = message.content.split()[1]
        fun=weatherTem(city)
        with open("my.json", "w") as file:
            data["messeges"] = fun
            json.dump(data, file, indent=3)


        await message.channel.send(f'Погода сегодня:\nОблачность: {weatherDet(city)}\nВлажность: {weatherHum(city)}\nТемпература в районе: {weatherTem(city)} градусов цельсия')

    if message.content.startswith('!stats'):
        await message.channel.send(f'статистика: {opening()}')




client.run(token)
