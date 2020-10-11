from telegram.ext import Updater, CommandHandler,MessageHandler,Filters
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton
import telegram

def hello(update, context):
    print(1)
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id


    s8 = '''Model: Samsung Galaxy S8 \nGPU: Mali-G71 MP20 \nOrqa kamera: 12 MP \nOld kamera: 8+2 MP \nROM: 64 GB \nRAM: 4GB \nBatareka: 3000 mAh \nTezkor quvvatlash: 15W'''
    s8p = '''Model: Samsung Galaxy S8+ \nCPU: 2.7 GHz, 1.7 GHz \nGPU: Mali-G71 \nOrqa kamera: 12 MP \nOld kamera: 8 MP \nROM: 64 GB \nRAM: 4GB \nBatareka: 3500 mAh \nTezkor quvvatlash: 15W'''
    s9 = '''Model: Samsung Galaxy S9 \nCPU: Samsung Exynos 9810 Octa \nOrqa kamera: 12 MP \nOld kamera: 8 MP \nROM: 64 GB \nRAM: 4GB \nBatareka: 3000 mAh \nKutish vaqti(h): 120'''
    s9p = '''Model: Samsung Galaxy S9+ \nCPU: Samsung Exynos 9 Octa 9810 \nOrqa kamera: 12 MP \nOld kamera: 12 MP \nROM: 64 GB \nRAM: 6GB \nBatareka: 3000 mAh \nYes (40% in 30 minutes)'''
    a10 = '''Model: Samsung Galaxy A10 \nGPU: Mali-G71 MP20 \nOrqa kamera: 13 MP \nOld kamera: 5 MP \nROM: 32 GB \nRAM: 2GB \nBatareka: 3400 mAh \nTezkor quvvatlash: 15W'''
    a10s = '''Model: Samsung Galaxy A10s \nCPU: 2 GHz, 1.5 GHz0 \nOrqa kamera: 13 MP \nOld kamera: 8 MP \nROM: 32 GB \nRAM: 3GB \nBatareka: 4000 mAh \nTezkor quvvatlash: 15W'''
    a20 = '''Model: Samsung Galaxy A20 \nCPU: 1.6 GHz, 1.35 GHz \nOrqa kamera: 13 MP \nOld kamera: 8 MP \nROM: 32 GB \nRAM: 4GB \nBatareka: 4000 mAh \nTezkor quvvatlash: 15W'''
    a20s = '''Model: Samsung Galaxy A20s \nCPU: 1.6 GHz, 1.35 GHz \nOrqa kamera: 13 MP \nOld kamera: 8 MP \nROM: 32 GB \nRAM: 4GB \nBatareka: 4000 mAh \nTezkor quvvatlash: 15W'''
    rn8 = '''Model: Redmi note 8 \nGPU: Mali-G71 MP20 \nOrqa kamera: 48+8+2+2 MP \nOld kamera: 13 MP \nROM: 64 GB \nRAM: 3GB \nBatareka: 4000 mAh \nTezkor quvvatlash: 18W'''
    rn8p = '''Model: Redmi note 8 pro \nGPU: Mali-G71 MP20 \nOrqa kamera: 48+8+2+2 MP \nOld kamera: 8+2 MP \nROM: 64 GB \nRAM: 4GB \nBatareka: 4500 mAh \nTezkor quvvatlash: 18W'''
    rn9 = '''Model: Redmi note 9 \nGPU: Mali-G71 MP20 \nOrqa kamera: 48+8+5+2 MP \nOld kamera: 13 MP \nROM: 64 GB \nRAM: 3GB \nBatareka: 5020 mAh \nTezkor quvvatlash: 18W'''
    rn9p = '''Model: Redmi note 9 pro S8+ \nQualcomm Snapdragon 720G \nOrqa kamera: 64+8+5+2 MP \nOld kamera: 16 MP \nROM: 128 GB \nRAM: 6GB \nBatareka: 5260mAh \nTezkor quvvatlash: 18W'''

    button = ReplyKeyboardMarkup(
        [
            ['Samsung'],
            ['Xiomi']

        ],
        resize_keyboard=True)
    
    Samsung_tur = ReplyKeyboardMarkup(  
        [
            ['Samsung Galaxy S Turlari va Xususiyatlari'],
            ['Samsung Galaxy A Turlari va Xususiyatlari'],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True
    )

    Samsung_S = ReplyKeyboardMarkup(
        [
            ['Samsung Galaxy S8','Samsung Galaxy S8+'],
            ['Samsung Galaxy S9','Samsung Galaxy S9+'],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True
    )

    Samsung_A = ReplyKeyboardMarkup(
        [
            ['Samsung Galaxy A10','Samsung Galaxy A10s'],
            ['Samsung Galaxy A20','Samsung Galaxy A20s'],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True
    )

    Xiomi = ReplyKeyboardMarkup(
        [
            ['Redmi note 8','Redmi note 8 pro'],
            ['Redmi note 9','Redmi note 9 pro'],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True
    )

    SGS = ReplyKeyboardMarkup(
        [
            ["Buyurtma berish"],
            ['Orqaga: Samsung Galaxy S'],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True
    )
    
    SGA = ReplyKeyboardMarkup(
        [
            ["Buyurtma berish"],
            ['Orqaga: Samsung Galaxy A'],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True
    )

    Redmi = ReplyKeyboardMarkup(
        [
            ["Buyurtma berish"],
            ['Orqaga: Xiomi'],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True
    )

    admin = ReplyKeyboardMarkup(
        [
            ['O`zingiz haqingizda malumot'],
            ["Admin bilan bog`lanish"],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True)

    contact = KeyboardButton(
        text='Contact',
        request_contact=True
    )

    location = KeyboardButton(
        text='Location',
        request_location=True
    )

    keyboard = ReplyKeyboardMarkup(
        [
            [contact],
            [location],
            ['Bosh Menuga qaytish']
        ],
        resize_keyboard=True
    )

    
    if text == 'Samsung':
        bot.sendMessage(chat_id,text='Tanlang 👇🏻',reply_markup=Samsung_tur)

    elif text == 'Bosh Menuga qaytish':
        bot.sendMessage(chat_id,text='Telefon bozoriga hush kelibsiz! Turini tanlang: Samsung va Xiomi 👇🏻',reply_markup=button)
        
    elif text == 'Xiomi':
        bot.sendMessage(chat_id,text='Tanlang va maqul kelsa hoziroq sotib oling! 👇🏻',reply_markup=Xiomi)

    elif text == 'Samsung Galaxy S Turlari va Xususiyatlari':
        bot.sendMessage(chat_id,text='Tanlang va maqul kelsa hoziroq sotib oling! 👇🏻',reply_markup=Samsung_S)

    elif text == 'Samsung Galaxy A Turlari va Xususiyatlari':
        bot.sendMessage(chat_id,text='Tanlang va maqul kelsa hoziroq sotib oling! 👇🏻',reply_markup=Samsung_A)

    elif text == 'Orqaga: Samsung Galaxy S':
        bot.sendMessage(chat_id,text='Tanlang va maqul kelsa hoziroq sotib oling! 👇🏻',reply_markup=Samsung_S)

    elif text == 'Orqaga: Samsung Galaxy A':
        bot.sendMessage(chat_id,text='Tanlang va maqul kelsa hoziroq sotib oling! 👇🏻',reply_markup=Samsung_A)

    elif text == 'Orqaga: Xiomi':
        bot.sendMessage(chat_id,text='Tanlang va maqul kelsa hoziroq sotib oling! 👇🏻',reply_markup=Xiomi)

    elif text == 'Samsung Galaxy S8':
        bot.sendMessage(chat_id,text=s8,reply_markup=SGS)

    elif text == 'Samsung Galaxy S8+':
        bot.sendMessage(chat_id,text=s8p,reply_markup=SGS)
    
    elif text == 'Samsung Galaxy S9':
        bot.sendMessage(chat_id,text=s9,reply_markup=SGS)
    
    elif text == 'Samsung Galaxy S9+':
        bot.sendMessage(chat_id,text=s9p,reply_markup=SGS)
    
    elif text == 'Samsung Galaxy A10':
        bot.sendMessage(chat_id,text=a10,reply_markup=SGA)
    
    elif text == 'Samsung Galaxy A10s':
        bot.sendMessage(chat_id,text=a10s,reply_markup=SGA)

    elif text == 'Samsung Galaxy A20':
        bot.sendMessage(chat_id,text=a20,reply_markup=SGA)
    
    elif text == 'Samsung Galaxy A20s':
        bot.sendMessage(chat_id,text=a20s,reply_markup=SGA)

    elif text == 'Redmi note 8':
        bot.sendMessage(chat_id,text=rn8,reply_markup=Redmi)

    elif text == 'Redmi note 8 pro':
        bot.sendMessage(chat_id,text=rn8p,reply_markup=Redmi)

    elif text == 'Redmi note 9':
        bot.sendMessage(chat_id,text=rn9,reply_markup=Redmi)
    
    elif text == 'Redmi note 9 pro':
        bot.sendMessage(chat_id,text=rn9p,reply_markup=Redmi)

    elif text == "Buyurtma berish":
        bot.sendMessage(chat_id,text='Kechirasiz hozircha dastafkamiz ishlamiyapti!',reply_markup=admin)

    elif text == "Admin bilan bog`lanish":
        bot.sendMessage(chat_id,text='https://t.me/JalilovJavohir',reply_markup=admin)
    
    elif text == 'O`zingiz haqingizda malumot':
        bot.sendMessage(chat_id,text='Contact and Location',reply_markup=keyboard)

def start(update,context):

    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id

    button = ReplyKeyboardMarkup(
        [
            ['Samsung'],
            ['Xiomi']
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text='Telefon bozoriga hush kelibsiz! Turini tanlang: Samsung va Xiomi 👇🏻',reply_markup=button)

def get_contact(update,context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id

    number = update.message.contact.phone_number
    firsname = update.message.contact.first_name

    bot.sendContact(1046157991,phone_number= number,first_name=firsname)

def get_location(update,context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id

    location = update.message.location

    bot.sendLocation(1046157991,location=location)

updater = Updater(token='1114424170:AAHakbVTr7nzgj6hOTSr9OrhTyaaLkunmd8',use_context=True)

updater.dispatcher.add_handler(CommandHandler('start',start))
updater.dispatcher.add_handler(MessageHandler(Filters.text,hello))

updater.dispatcher.add_handler(MessageHandler(Filters.contact,get_contact))
updater.dispatcher.add_handler(MessageHandler(Filters.location,get_location))

updater.start_polling()
updater.idle()
