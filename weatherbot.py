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
    if response:
        data = response.json()
        joy = data['name']
        temp = data['main']['temp']
        descr = data['weather'][0]['description']
        wind = data['wind']['speed']
        icon = data['weather'][0]['icon']
        pprint(data)

        if icon=='01d' or icon=='01n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° ☀'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)

        if icon=='02d' or icon=='02n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌤'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)
    
        if icon=='03d' or icon=='03n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌥'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)
 
        if icon=='04d' or icon=='04n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° ☁️'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)
       
        if icon=='09d' or icon=='09n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌦'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)
        
        if icon=='10d' or icon=='10n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌧'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)
       
        if icon=='11d' or icon=='11n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌩'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)
        
        if icon=='13d' or icon=='13n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° ❄️'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)
  
        if icon=='50d' or icon=='50n':
            all_ = 'from: '+str(joy)+'\nTemp: '+str(temp)+'° 🌫'+'\ndescription: '+str(descr)+'\nWind: '+str(wind)+" m/s"
            bot.sendMessage(chat_id,text=all_)

        
    else:
        bot.sendMessage(chat_id,text='None')

updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.dispatcher.add_handler(MessageHandler(Filters.location,get_location))

updater.start_polling()
updater.idle()