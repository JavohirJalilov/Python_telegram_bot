import requests
import json
import os
from pprint import pprint
KEY = os.environ["WEATHER_KEY"]

pyload = {
    'lat':39.830313,
    'lon':67.424598,
    'units':'metric',
    'appid':KEY
}
response = requests.get('https://api.openweathermap.org/data/2.5/weather',params=pyload)
data = response.json()

pprint(data)