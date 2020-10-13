from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
import telegram
import os

TOKEN = os.environ['frilanser']

def get_photo(update, context):
    bot = context.bot
    chat_id = update.message.chat.id 
    file_id = update.message.photo[0].file_id
    
    bot.sendPhoto(
        chat_id=chat_id,
        photo=file_id,
        caption=f'https://t.me/JalilovJavohir\nFile_id: {file_id}'
    )

def get_sticker(update, context):
    bot = context.bot
    chat_id = update.message.chat.id 
    file_id = update.message.sticker.file_id
    
    bot.sendSticker(
        chat_id=chat_id,
        sticker=file_id
    )
    bot.sendMessage(chat_id,text=f'file_id: {file_id}')

updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.photo,get_photo))
updater.dispatcher.add_handler(MessageHandler(Filters.sticker,get_sticker))


updater.start_polling()
updater.idle()