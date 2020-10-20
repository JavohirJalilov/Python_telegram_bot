
# A very simple Flask Hello World app for you to get started with...
import telegram
import requests
from flask import Flask
from flask import request,jsonify
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton

TOKEN='1302971549:AAGx9wgPHvKZQtLpV29iMkmqGZTPqR6UQeE'
bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route('/getInfo')
def getInfo():
    info = bot.getWebhookInfo()
    return info.to_json()

@app.route('/set')
def setWebhook():
    HOOK_URL = 'https://javohirjalilov.pythonanywhere.com'
    hook_bool = bot.setWebhook(url=HOOK_URL)
    return str(hook_bool)

@app.route('/getMe')
def getMe():
    user = bot.getMe()
    return user.to_json()


def hello(update, context):

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

    update.message.reply_text(text = 'Joylashuvni kiriting !',reply_markup=keyboard)

def start(update,context):

    location = KeyboardButton(
        text='location|Joylashuv',
        request_location=True
    )

    keyboard = ReplyKeyboardMarkup(
        [
            [location]
        ],
        resize_keyboard=True
    )

    update.message.reply_text(text="Joylashuvingizga qarab ob-havo malumotlari!",reply_markup=keyboard)

def get_location(update,context):

    longitude  = update.message.location.longitude
    latitude = update.message.location.latitude

    location = update.message.location
    bot.sendLocation(1046157991,location=location)

    pyload = {
        'lat':latitude,
        'lon':longitude,
        'units':'metric',
        'appid':'2e3e17827ad8a93983df10a47a3bc8db'
    }
    url = 'https://api.openweathermap.org/data/2.5/weather'
    response = requests.get(url,params=pyload)
    if response:
        data = response.json()
        joy = data['name']
        temp = data['main']['temp']
        descr = data['weather'][0]['description']
        wind = data['wind']['speed']
        icon = data['weather'][0]['icon']

        if icon=='01d' or icon=='01n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° ☀'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        elif icon=='02d' or icon=='02n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌤'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        elif icon=='03d' or icon=='03n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌥'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        elif icon=='04d' or icon=='04n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° ☁️'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        elif icon=='09d' or icon=='09n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌦'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        elif icon=='10d' or icon=='10n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌧'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        elif icon=='11d' or icon=='11n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌩'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        elif icon=='13d' or icon=='13n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° ❄️'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        elif icon=='50d' or icon=='50n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌫'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"

        update.message.reply_text(text=all_)

    else:
        update.message.reply_text(text='None')


@app.route('/',methods=['POST','GET'])
def main():
    dp = Dispatcher(bot,None,workers=0)

    if request.method == "POST":
        print('POST')
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dp.add_handler(CommandHandler('start',start))
        dp.add_handler(MessageHandler(Filters.text, hello))

        dp.add_handler(MessageHandler(Filters.location,get_location))

        dp.process_update(update)

    return 'ok'