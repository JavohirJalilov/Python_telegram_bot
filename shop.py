from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,InlineQueryHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton,InputTextMessageContent,InlineQueryResultArticle,KeyboardButton
import telegram

import os

TOKEN = os.environ['inline']

def start(update,context):
    first_name = update.message.from_user.first_name
    text = f'Hush kelibsiz {first_name} !\n biznig online do`kondan Noutbook 💻 va kompyuterlar 🖥, \nkompyuter extiyot qismlari ⌨️\nKompyuter qo`shimcha qurilmalarini topishingiz mumkin 🖨.\nMarhamt !'
    katalog = KeyboardButton(text='📘 Katalog')
    savat = KeyboardButton(text='🛒 Savat')
    reply_markup = ReplyKeyboardMarkup(
        [
            [katalog,savat]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text=text,reply_markup=reply_markup) 
def katalog(update,context):
    text = 'Bizda mavjud maxsulotlar:'
    monitor =  InlineKeyboardButton(text='🖥 Monitor',callback_data='monitor')
    printer = InlineKeyboardButton(text='🖨 Printer',callback_data='printer')
    extiyotqismlar = InlineKeyboardButton(text='⚙️ Extiyot qismlar',callback_data='extiyot qismalar')
    reply_markup = InlineKeyboardMarkup(
        [
            [monitor,printer],
            [extiyotqismlar]
        ]
    )
    update.message.reply_text(text=text,reply_markup=reply_markup) 

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📘 Katalog'),katalog))
#updater.dispatcher.add_handler(MessageHandler(Filters.text('🛒 Savat'),savat))


updater.start_polling()
updater.idle()