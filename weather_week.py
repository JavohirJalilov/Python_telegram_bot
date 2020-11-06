import requests
import json
from pprint import pprint
from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
import telegram
from pprint import pprint

def hello(update, context):
    bot = context.bot
    chat_id = update.message.chat.id
    location = KeyboardButton(
        text='Location|Joylashuv',
        request_location=True
    )
    keyboard = ReplyKeyboardMarkup(
        [
            [location]
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text = 'Joylashuvni kiriting !',reply_markup=keyboard)

def start(update,context):
    bot = context.bot 
    chat_id = update.message.chat.id 
    location = KeyboardButton(
        text='Location|Joylashuv 📍',
        request_location=True
    )
    keyboard = ReplyKeyboardMarkup(
        [
            [location]
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text="Location|Joylashuv 📍 kiriting.\nBir haftalik ob-havo malumotlari !",reply_markup=keyboard)

def get_location(update,context):
    bot= context.bot 
    chat_id = update.message.chat.id 
    # text = update.message.text 
    longitude  = update.message.location.longitude 
    latitude = update.message.location.latitude 
    # location = update.message.location
    # bot.sendLocation(1046157991,location=location)
    pyload = {
        'lat':latitude,
        'lon':longitude,
        'units':'metric',
        'appid':'2e3e17827ad8a93983df10a47a3bc8db'
    }
    url = 'https://api.openweathermap.org/data/2.5/onecall'
    response = requests.get(url,params=pyload)
    data = response.json()
    # print(data)
    # if response:
    #     data = response.json()
    #     joy = data['name']
    #     temp = data['main']['temp']
    #     descr = data['weather'][0]['description']
    #     wind = data['wind']['speed']
    #     icon = data['weather'][0]['icon']
    #     pprint(data)
    bot.sendMessage(chat_id,text=week(data,response),parse_mode="HTML")
    
def week(data,response):
    time = requests.get(f"http://worldtimeapi.org/api/timezone/{data['timezone']}")
    week = time.json()
    day = week['datetime'][0:10]
    time = week['datetime'][11:17]
    day_of_week = week['day_of_week']
    if day_of_week == 1:
        if response:
            loc = data['timezone']
            all_ = f'Joylashuvingiz 📍: <i><b>{loc}</b></i>\n\n<u>{day}</u>  <u>{time}</u>\n'
            for i in range(8):
                temp_max = round(data['daily'][i]['temp']['max'])
                temp_min = round(data['daily'][i]['temp']['min'])
                temp_eve = round(data['daily'][i]['temp']['eve'])
                temp_morn = round(data['daily'][i]['temp']['morn'])
                temp_night = round(data['daily'][i]['temp']['night'])
                # descr = data['daily'][i]['weather'][0]['description']
                icon = data['daily'][i]['weather'][0]['icon']
                # main = data['daily'][i]['weather'][0]['main']
                wind = round(data['daily'][i]['wind_speed'])
                if i == 0:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Bugun</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min:{temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Bugun</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Bugun</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Bugun</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Bugun</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Bugun</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Bugun</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Bugun</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C -  {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Bugun</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 1:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: Ertaga (<i>Seshanba</i>): Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 2:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Chorshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Chorshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Chorshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Chorshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Chorshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 3:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Payshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Payshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Payshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Payshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Payshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Payshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Payshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Payshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Payshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 4:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Juma</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Juma</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Juma</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Juma</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Juma</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Juma</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Juma</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Juma</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Juma</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 5:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>shanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>shanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>shanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>shanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>shanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\n Kechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>shanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>shanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>shanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>shanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 6:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Yakshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Yakshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Yakshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Yakshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Yakshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 7:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Dushanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Dushanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Dushanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Dushanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Dushanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Dushanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Dushanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Dushanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Dushanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"     
            return all_     
        else:
            return 'None'
    elif day_of_week == 2:
        if response:
            loc = data['timezone']
            all_ = f'Joylashuvingiz 📍: <i><b>{loc}</b></i>\n\n<u>{day}</u>  <u>{time}</u>\n'
            for i in range(8):
                temp_max = round(data['daily'][i]['temp']['max'])
                temp_min = round(data['daily'][i]['temp']['min'])
                temp_eve = round(data['daily'][i]['temp']['eve'])
                temp_morn = round(data['daily'][i]['temp']['morn'])
                temp_night = round(data['daily'][i]['temp']['night'])
                # descr = data['daily'][i]['weather'][0]['description']
                icon = data['daily'][i]['weather'][0]['icon']
                # main = data['daily'][i]['weather'][0]['main']
                wind = round(data['daily'][i]['wind_speed'])
                if i == 0:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Bugun</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min:{temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Bugun</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Bugun</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Bugun</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Bugun</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Bugun</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Bugun</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Bugun</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C -  {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Bugun</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 1:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: Ertaga (<i>Chorshanba</i>): Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 2:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Payshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Payshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Payshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Payshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Payshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Payshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Payshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Payshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Payshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 3:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Juma</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Juma</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Juma</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Juma</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Juma</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Juma</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Juma</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Juma</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Juma</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 4:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Shanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Shanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Shanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Shanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Shanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Shanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Shanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Shanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Shanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 5:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Yakshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Yakshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\n Kechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Yakshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Yakshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Yakshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 6:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Dushanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Dushanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Dushanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Dushanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Dushanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Dushanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Dushanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Dushanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Dushanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 7:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Seshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Seshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Seshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Seshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Seshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Seshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Seshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Seshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Seshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"     
            return all_     
        else:
            return 'None'
    elif day_of_week == 3:
        if response:
            loc = data['timezone']
            all_ = f'Joylashuvingiz 📍: <i><b>{loc}</b></i>\n\n<u>{day}</u>  <u>{time}</u>\n'
            for i in range(8):
                temp_max = round(data['daily'][i]['temp']['max'])
                temp_min = round(data['daily'][i]['temp']['min'])
                temp_eve = round(data['daily'][i]['temp']['eve'])
                temp_morn = round(data['daily'][i]['temp']['morn'])
                temp_night = round(data['daily'][i]['temp']['night'])
                # descr = data['daily'][i]['weather'][0]['description']
                icon = data['daily'][i]['weather'][0]['icon']
                # main = data['daily'][i]['weather'][0]['main']
                wind = round(data['daily'][i]['wind_speed'])
                if i == 0:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Bugun</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min:{temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Bugun</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Bugun</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Bugun</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Bugun</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Bugun</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Bugun</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Bugun</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C -  {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Bugun</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 1:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: Ertaga (<i>Payshanba</i>): Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 2:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Juma</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Juma</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Juma</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Juma</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Juma</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Juma</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Juma</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Juma</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Juma</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 3:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Shanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Shanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Shanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Shanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Shanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Shanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Shanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Shanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Shanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 4:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Yakshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Yakshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Yakshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Yakshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Yakshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 5:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Dushanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Dushanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Dushanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Dushanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Dushanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\n Kechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Dushanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Dushanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Dushanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Dushanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 6:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Seshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Seshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Seshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Seshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Chorshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Seshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Seshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Seshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Seshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 7:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Chorshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Chorshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Chorshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Chorshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Chorshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"     
            return all_     
        else:
            return 'None'
    if day_of_week == 4:
        if response:
            loc = data['timezone']
            all_ = f'Joylashuvingiz 📍: <i><b>{loc}</b></i>\n\n<u>{day}</u>  <u>{time}</u>\n'
            for i in range(8):
                temp_max = round(data['daily'][i]['temp']['max'])
                temp_min = round(data['daily'][i]['temp']['min'])
                temp_eve = round(data['daily'][i]['temp']['eve'])
                temp_morn = round(data['daily'][i]['temp']['morn'])
                temp_night = round(data['daily'][i]['temp']['night'])
                # descr = data['daily'][i]['weather'][0]['description']
                icon = data['daily'][i]['weather'][0]['icon']
                # main = data['daily'][i]['weather'][0]['main']
                wind = round(data['daily'][i]['wind_speed'])
                if i == 0:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Bugun</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min:{temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Bugun</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Bugun</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Bugun</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Bugun</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Bugun</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Bugun</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Bugun</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C -  {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Bugun</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 1:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: Ertaga (<i>Juma</i>): Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 2:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Shanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Shanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Shanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Shanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Shanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Shanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Shanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Shanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Shanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 3:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Yakshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Yakshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Yakshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Yakshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Yakshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 4:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Dushanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Dushanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Dushanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Dushanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Dushanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Dushanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Dushanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Dushanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Dushanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 5:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Seshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Seshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Seshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Seshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Seshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\n Kechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Seshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Seshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Seshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Seshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 6:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Chorshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Chorshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Chorshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Chorshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Chorshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 7:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Payshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Payshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Payshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Payshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Payshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Payshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Payshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Payshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Payshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"     
            return all_     
        else:
            return 'None'

    
        
    elif day_of_week == 5:
        if response:
            loc = data['timezone']
            all_ = f'Joylashuvingiz 📍: <i><b>{loc}</b></i>\n\n<u>{day}</u>  <u>{time}</u>\n'
            for i in range(8):
                temp_max = round(data['daily'][i]['temp']['max'])
                temp_min = round(data['daily'][i]['temp']['min'])
                temp_eve = round(data['daily'][i]['temp']['eve'])
                temp_morn = round(data['daily'][i]['temp']['morn'])
                temp_night = round(data['daily'][i]['temp']['night'])
                # descr = data['daily'][i]['weather'][0]['description']
                icon = data['daily'][i]['weather'][0]['icon']
                # main = data['daily'][i]['weather'][0]['main']
                wind = round(data['daily'][i]['wind_speed'])
                if i == 0:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Bugun</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min:{temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Bugun</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Bugun</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Bugun</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Bugun</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Bugun</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Bugun</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Bugun</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C -  {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Bugun</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 1:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: Ertaga (<i>Shanba</i>): Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 2:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Yakshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Yakshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Yakshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Yakshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Yakshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 3:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Dushanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Dushanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Dushanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Dushanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Dushanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Dushanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Dushanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Dushanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Dushanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 4:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Seshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Seshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Seshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Seshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Seshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Seshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Seshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Seshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Seshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 5:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Chorshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Chorshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\n Kechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Chorshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Chorshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Chorshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 6:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Payshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Payshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Payshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Payshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Payshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Payshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Payshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Payshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Payshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 7:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Juma</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Juma</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Juma</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Juma</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Juma</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Juma</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Juma</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Juma</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Juma</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"     
            return all_     
        else:
            return 'None'
    elif day_of_week == 6:
        if response:
            loc = data['timezone']
            all_ = f'Joylashuvingiz 📍: <i><b>{loc}</b></i>\n\n<u>{day}</u>  <u>{time}</u>\n'
            for i in range(8):
                temp_max = round(data['daily'][i]['temp']['max'])
                temp_min = round(data['daily'][i]['temp']['min'])
                temp_eve = round(data['daily'][i]['temp']['eve'])
                temp_morn = round(data['daily'][i]['temp']['morn'])
                temp_night = round(data['daily'][i]['temp']['night'])
                # descr = data['daily'][i]['weather'][0]['description']
                icon = data['daily'][i]['weather'][0]['icon']
                # main = data['daily'][i]['weather'][0]['main']
                wind = round(data['daily'][i]['wind_speed'])
                if i == 0:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Bugun</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min:{temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Bugun</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Bugun</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Bugun</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Bugun</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Bugun</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Bugun</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Bugun</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C -  {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Bugun</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 1:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: Ertaga (<i>Yakshanba</i>): Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 2:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Dushanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Dushanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Dushanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Dushanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Dushanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Dushanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Dushanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Dushanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Dushanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 3:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Seshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Seshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Seshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Seshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Seshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Seshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Seshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Seshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Seshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 4:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Chorshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Chorshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Chorshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Chorshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Chorshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 5:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Payshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Payshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Payshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Payshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Payshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\n Kechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Payshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Payshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Payshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Payshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 6:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Juma</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Juma</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Juma</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Juma</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Juma</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Juma</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Juma</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Juma</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Juma</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 7:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Shanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Shanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Shanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Shanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Shanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Shanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Shanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Shanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Shanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"     
            return all_     
        else:
            return 'None'
    elif day_of_week == 7:
        if response:
            loc = data['timezone']
            all_ = f'Joylashuvingiz 📍: <i><b>{loc}</b></i>\n\n<u>{day}</u>  <u>{time}</u>\n'
            for i in range(8):
                temp_max = round(data['daily'][i]['temp']['max'])
                temp_min = round(data['daily'][i]['temp']['min'])
                temp_eve = round(data['daily'][i]['temp']['eve'])
                temp_morn = round(data['daily'][i]['temp']['morn'])
                temp_night = round(data['daily'][i]['temp']['night'])
                # descr = data['daily'][i]['weather'][0]['description']
                icon = data['daily'][i]['weather'][0]['icon']
                # main = data['daily'][i]['weather'][0]['main']
                wind = round(data['daily'][i]['wind_speed'])
                if i == 0:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Bugun</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min:{temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Bugun</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Bugun</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Bugun</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Bugun</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Bugun</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Bugun</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Bugun</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C -  {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Bugun</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 1:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: Ertaga (<i>Dushanba</i>): Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 2:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Seshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Seshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Seshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Seshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Seshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Seshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Seshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Seshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Seshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 3:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Chorshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Chorshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Chorshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Chorshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Chorshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Chorshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Chorshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 4:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Payshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Payshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Payshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Payshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Payshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Payshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Payshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Payshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Payshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 5:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Juma</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha:{temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Juma</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Juma</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Juma</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Juma</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\n O`rtacha: {temp_eve}°C 🌦\n Kechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Juma</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Juma</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Juma</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Juma</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 6:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Shanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Shanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Shanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Shanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Shanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Shanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Shanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Shanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Shanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"

                elif i == 7:
                    if icon=='01d' or icon=='01n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ochiq osmon\nErtalab: {temp_morn}°C ☀\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☀\nO`rtacha: {temp_eve}°C ☀\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='02d' or icon=='02n':
                        all_ += f"Kun: <i>Yakshanba</i>: Ozgina buluti\nErtalab: {temp_morn}°C 🌤\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌤\nO`rtacha: {temp_eve}°C 🌤\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='03d' or icon=='03n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tarqoq bulutli\nErtalab: {temp_morn}°C 🌥\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌥\nO`rtacha: {temp_eve}°C 🌥\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='04d' or icon=='04n':
                        all_ += f"Kun: <i>Yakshanba</i>: Buzilgan buluti\nErtalab: {temp_morn}°C ☁️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ☁️\nO`rtacha: {temp_eve}°C ☁️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='09d' or icon=='09n':
                        all_ += f"Kun: <i>Yakshanba</i>: yomg'ir yog'ish extimoli bor\nErtalab: {temp_morn}°C 🌦\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌦\nO`rtacha: {temp_eve}°C 🌦\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='10d' or icon=='10n':
                        all_ += f"Kun: <i>Yakshanba</i>: Yomg'ir\nErtalab: {temp_morn}°C 🌧\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌧\nO`rtacha: {temp_eve}°C 🌧\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='11d' or icon=='11n':
                        all_ += f"Kun: <i>Yakshanba</i>: Momaqaldiroq\nErtalab: {temp_morn}°C 🌩\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌩\nO`rtacha: {temp_eve}°C 🌩\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='13d' or icon=='13n':
                        all_ += f"Kun: <i>Yakshanba</i>: Qor\nErtalab: {temp_morn}°C ❄️\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C ❄️\nO`rtacha: {temp_eve}°C ❄️\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"
                    elif icon=='50d' or icon=='50n':
                        all_ += f"Kun: <i>Yakshanba</i>: Tuman\nErtalab: {temp_morn}°C 🌫\nKun bo`yi: max-min: {temp_max}°C - {temp_min}°C 🌫\nO`rtacha: {temp_eve}°C 🌫\nKechqurun: {temp_night}°C \nShamol: {wind} m/s\n\n"     
            return all_     
        else:
            return 'None'
    

updater = Updater(token='1495856262:AAHH_kr8rzuHThwRXec5yEPQkJWNloSt6sQ')
updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))
updater.dispatcher.add_handler(MessageHandler(Filters.location,get_location))

updater.start_polling()
updater.idle()