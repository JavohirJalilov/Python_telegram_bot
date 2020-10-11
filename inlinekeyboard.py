from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
import telegram
import os

TOKEN = os.environ["TOKEN"]

def hello(update, context):
    print(1)
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    
    button = InlineKeyboardButton(
        text='inline'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [button]
        ]
    )

    bot.sendMessage(chat_id,text = text,reply_markup=keyboard)

updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.start_polling()
updater.idle()