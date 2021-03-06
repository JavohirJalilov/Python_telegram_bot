from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
import telegram
import requests
import os

TOKEN = os.environ["ism"]

def start(update,context):
    update.message.reply_text(text='Marhamt! Ismni kiriting.')

def hello(update, context):
    bot = context.bot
    text = update.message.text
    res = requests.get(f'https://ismlar.com/search/{text}')
    print(res.status_code)
    s = res.text
    
    x = s.index('class="mb-3"')
    y = s.index('</h3>',x)

    x += 111 + len(text)
    tur = s[x:y]

    if tur == 'Исм маъносини топиш учун буюртма бериш':
        mano = 'Afsus, Bunday ism hozircha bizda mavjud emas'
        update.message.reply_text(text=mano) 
    else:
        i = s.index('class="text-size-5"')
        l = s.index('</p>',i)
        i = i+20

        k = s.index('class="fas fa-tag"')
        j = s.index('</a>',k)
        k+=23
        tur = s[k:j]
        mano = s[i:l]
        text=f'<u><i>{tur}</i></u>'+'\n'+mano
        update.message.reply_text(text=f'<b>{text}</b>',parse_mode='HTML')

updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.start_polling()
updater.idle()