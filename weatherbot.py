import requests
import json
from pprint import pprint
from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
import telegram
from pprint import pprint
import os
KEY = os.environ["WEATHER_KEY"]

TOKEN = os.environ["token"]

def hello(update, context):

    bot = context.bot
    chat_id = update.message.chat.id
    text = update.message.text

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
        text='location|Joylashuv',
        request_location=True
    )

    keyboard = ReplyKeyboardMarkup(
        [
            [location]
        ],
        resize_keyboard=True
    )

    bot.sendMessage(chat_id,text="Joylashuvingizga qarab ob-havo malumotlari!",reply_markup=keyboard)

def get_location(update,context):
    bot= context.bot 
    chat_id = update.message.chat.id 
    text = update.message.text 

    longitude  = update.message.location.longitude 
    latitude = update.message.location.latitude 

    location = update.message.location
    bot.sendLocation(1046157991,location=location)


    pyload = {
        'lat':latitude,
        'lon':longitude,
        'units':'metric',
        'appid':KEY
    }
    response = requests.get('https://api.openweathermap.org/data/2.5/weather',params=pyload)
    data = response.json()
    
    joy = data['name']
    temp = data['main']['temp']
    descr = data['weather'][0]['description']
    wind = data['wind']['speed']
    all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
    bot.sendMessage(chat_id,text=all_)


updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.dispatcher.add_handler(MessageHandler(Filters.location,get_location))

updater.start_polling()
updater.idle()