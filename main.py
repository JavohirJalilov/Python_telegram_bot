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

    bot.sendMessage(chat_id,text = text,reply_markup=keyboard)

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

    bot.sendMessage(chat_id,text="contact yuborish",reply_markup=keyboard)

def get_contact(update,context):
    bot= context.bot 
    chat_id = update.message.chat.id 
    text = update.message.text 

    contact = update.message.contact.phone_number
    firstname = update.message.contact.first_name
    Number = firstname+"\n"+contact
    print(Number)

    f = open('text.txt','w')
    f.write(Number+'\n')
    f.close()

def get_location(update,context):
    bot= context.bot 
    chat_id = update.message.chat.id 
    text = update.message.text 

    l1 = update.message.location.longitude
    l2 = update.message.location.latitude
    s = str(l2)+','+str(l1)
    print(s)

updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.dispatcher.add_handler(MessageHandler(Filters.contact,get_contact))
updater.dispatcher.add_handler(MessageHandler(Filters.location,get_location))


updater.start_polling()
updater.idle()