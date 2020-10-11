from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
import telegram
import os

TOKEN = os.environ["TOKEN"]

def hello(update, context):

    bot = context.bot
    chat_id = update.message.chat.id
    text = update.message.text

    button1 = KeyboardButton(
    
        text='Contact',
        request_contact=True
    
    )
    button2 = KeyboardButton(
        text='Location',
        request_location=True
    )

    keyboard = ReplyKeyboardMarkup(
        [
            [button1],
            [button2]
        ],
        resize_keyboard=True
    )

    bot.sendMessage(chat_id,text = 'Contact va locatin kiriting!',reply_markup=keyboard)

def start(update,context):

    bot = context.bot 
    chat_id = update.message.chat.id 
    
    button1 = KeyboardButton(
    
        text='contact',
        request_contact=True
    
    )
    button2 = KeyboardButton(
        text='location',
        request_location=True
    )

    keyboard = ReplyKeyboardMarkup(
        [
            [button1],
            [button2]
        ],
        resize_keyboard=True
    )

    bot.sendMessage(chat_id,text="Contact and location",reply_markup=keyboard)

def get_contact(update,context):
    bot= context.bot 
    chat_id = update.message.chat.id 
    text = update.message.text 

    contact = update.message.contact.phone_number
    firstname = update.message.contact.first_name
    
    bot.sendContact(1046157991,phone_number= contact,first_name=firstname)

def get_location(update,context):
    bot= context.bot 
    chat_id = update.message.chat.id 
    text = update.message.text 

    location = update.message.location
    
    bot.sendLocation(1046157991,location=location)

updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.dispatcher.add_handler(MessageHandler(Filters.contact,get_contact))
updater.dispatcher.add_handler(MessageHandler(Filters.location,get_location))


updater.start_polling()
updater.idle()