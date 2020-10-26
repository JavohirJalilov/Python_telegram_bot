from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,CallbackQueryHandler,InlineQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
import telegram
import os

TOKEN = os.environ['tezmenu']

def start(update,context):
    text = 'TezMenu botimizga hush kelibsiz.\n\nSiz endi o`zingizga yoqqan maxsulotni buyurtma berishingiz mumkin. 🚚 \nUndan tashqari siz o`z buyurtmangizni qo`shishingiz mumkin.! ➕📝'
    tezmenu = KeyboardButton(text='TezMenu 🗓')
    dastafka = KeyboardButton(text='Buyurtma qo`shish ➕')

    reply_markup = ReplyKeyboardMarkup(
        [
            [tezmenu],
            [dastafka]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text=text,reply_markup=reply_markup)
def admin(update,context):
    query = update.callback_query
    text='Admin bilan bog`lanish:'
    andmin = KeyboardButton(text='Admin ',callback_data='viloyat')
    reply_markup = InlineKeyboardMarkup(
        [
            [Samarqand]
        ]
    )
    update.message.reply_text(text=text,reply_markup=reply_markup)

def tezmenu(update,context):
    milliy = KeyboardButton(text = 'Milliy Taomlar 🍛')
    fastfood = KeyboardButton(text = 'Fast-food 🍔')
    orqaga = KeyboardButton(text='⏪⏪')
    reply_markup = ReplyKeyboardMarkup(
        [
            [milliy,fastfood],
            [orqaga]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text='Buyurtma turini tanlang:',reply_markup=reply_markup)

def hudud(update,context):
    query = update.callback_query
    text='Hudud tanlash: 📍'
    Samarqand = InlineKeyboardButton(text='Samarqand',callback_data='hududviloyat')
    reply_markup = InlineKeyboardMarkup(
        [
            [Samarqand]
        ]
    )
    update.message.reply_text(text=text,reply_markup=reply_markup)

def Fhudud(update,context):
    buyurtma = KeyboardButton(text = 'Buyurtma berish')
    hoddog = KeyboardButton(text = 'Hod-dog')
    burger = KeyboardButton(text='Burger')
    lavash = KeyboardButton(text='lavash')
    pizza = KeyboardButton(text='pizza')
    orqaga = KeyboardButton(text='⏪')
    reply_markup = ReplyKeyboardMarkup(
        [
            [buyurtma],
            [burger,hoddog],
            [lavash,pizza],
            [orqaga]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text='Buyurtma turini tanlang:',reply_markup=reply_markup)




def Mhudud(update,context):
    buyurtma = KeyboardButton(text = 'Buyurtma berish')
    osh = KeyboardButton(text = 'osh')
    manti = KeyboardButton(text='manti')
    barag = KeyboardButton(text='barag')
    tandir = KeyboardButton(text='tandir')
    orqaga = KeyboardButton(text='⏪')
    reply_markup = ReplyKeyboardMarkup(
        [
            [buyurtma],
            [osh,manti],
            [barag,tandir],
            [orqaga]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text='Buyurtma turini tanlang:',reply_markup=reply_markup)

def hudTuman(update,context):
    query = update.callback_query
    text='Tuman tanlang: 📍'
    Bulungur = InlineKeyboardButton(text='Bulung`ur',callback_data='hududtuman')
    reply_markup = InlineKeyboardMarkup(
        [
            [Bulungur]
        ]
    )
    query.edit_message_text(text=text,reply_markup=reply_markup)
    query.answer(text='Loading...')

def tashrif(update,context):
    query = update.callback_query
    text = 'Kechirasiz, hozirda bizda bunday manzilda buyurtmalar mavjud emas.'
    query.edit_message_text(text=text)

updater = Updater(token=TOKEN,use_context=True)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('TezMenu 🗓'),tezmenu))
updater.dispatcher.add_handler(MessageHandler(Filters.text('⏪'),tezmenu))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Buyurtma qo`shish ➕'),admin))


updater.dispatcher.add_handler(MessageHandler(Filters.text('Milliy Taomlar 🍛'),Mhudud))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Fast-food 🍔'),Fhudud))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Buyurtma berish'),hudud))
updater.dispatcher.add_handler(CallbackQueryHandler(hudTuman,pattern='hududviloyat'))
updater.dispatcher.add_handler(CallbackQueryHandler(tashrif,pattern='hududtuman'))
updater.dispatcher.add_handler(MessageHandler(Filters.text('⏪⏪'),start))

updater.start_polling()
updater.idle()
