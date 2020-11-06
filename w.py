import requests
import json
import os
from pprint import pprint
# KEY = os.environ["WEATHER_KEY"]

pyload = {
    'lat':39.830313,
    'lon':67.424598,
    'units':'metric',
    'appid':'2e3e17827ad8a93983df10a47a3bc8db'
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall',params=pyload)
data = response.json()
#bugun
current = data['current']['temp']
i = 0
daily = data['daily']
# for i in daily:
#     pprint(i['temp'])
# pprint(data['current']['temp'])
#https://api.openweathermap.org/data/2.5/weather

time = requests.get(f"http://worldtimeapi.org/api/timezone/{data['timezone']}")
data = time.json()
pprint(data)