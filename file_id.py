from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton

import telegram
import os

TOKEN = os.environ['frilanser']

#rn9 = '''Model: Redmi note 9 \nGPU: Mali-G71 MP20 \nOrqa kamera: 48+8+5+2 MP \nOld kamera: 13 MP \nROM: 64 GB \nRAM: 3GB \nBatareka: 5020 mAh \nTezkor quvvatlash: 18W'''

#file_id = 'AgACAgIAAxkBAAIBwl-FYSs6GWAwD6YvT9H9H8_oH5YDAAJzrzEbgAcoSHs_eiEoSoG0QWkYlS4AAwEAAwIAA3kAA8A4BQABGwQ'
#bot = telegram.Bot(TOKEN)
#data = bot.getUpdates()
#file_photo = open('redmi.jpg','rb')

#print(data[-1])
#bot.sendPhoto(
#    chat_id=1046157991,
#    photo=file_id,
#    caption=rn9
#)

def get_photo(update, context):
    bot = context.bot
    chat_id = update.message.chat.id 
    file_id = update.message.photo[0].file_id
    
    bot.sendPhoto(
        chat_id=chat_id,
        photo=file_id,
        caption=f'https://t.me/JalilovJavohir\nFile_id: {file_id}'
    )

updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.photo,get_photo))


updater.start_polling()
updater.idle()