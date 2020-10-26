from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,InlineQueryHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton,InputTextMessageContent,InlineQueryResultArticle,KeyboardButton
import telegram

import os

TOKEN = os.environ['TOKEN']

def start(update,context):
    first_name = update.message.from_user.first_name
    text = f'Hush kelibsiz {first_name} !\n biznig online do`kondan Noutbook 💻 va kompyuterlar 🖥, \nkompyuter extiyot qismlari ⌨️\nKompyuter qo`shimcha qurilmalarini topishingiz mumkin 🖨.\nMarhamt !'
    interfaoldoska = KeyboardButton(text='Interfaol doska')
    interaktivdispley = KeyboardButton(text='Interaktiv displey')
    kompyuter = KeyboardButton(text='Kompyuter(pc) 🖥')
    monoblok = KeyboardButton(text='Monoblok')
    notebook = KeyboardButton(text='Notebook 💻')
    extiyotqismlar = KeyboardButton(text='Extiyot qismlar ⚙️')
    monitor = KeyboardButton(text='Monitor 🖥')
    printer = KeyboardButton(text='Printer 🖨')
    aksesuar = KeyboardButton(text='Aksesuar 💾')
    
    keyboard = ReplyKeyboardMarkup(
        [
            [kompyuter,notebook],
            [interaktivdispley,interfaoldoska],
            [monoblok,monitor],
            [extiyotqismlar,printer],
            [aksesuar]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text=text,reply_markup=keyboard) 

def kompyuter(update,context):
    hp = InlineKeyboardButton(text='HP',switch_inline_query_current_chat='hp')
    legion = InlineKeyboardButton(text='Legion',switch_inline_query_current_chat='legion')
    zotac = InlineKeyboardButton(text='Zotac',switch_inline_query_current_chat='zotac')
    
    reply_markup = InlineKeyboardMarkup(
        [
            [hp,legion],
            [zotac]
        ]
    )
    update.message.reply_text(text='Kompyuterlar (PC)🖥:',reply_markup=reply_markup)
def hp(update,context):
    text1='HP 460-a210ur MicroTower (SUS) \nIntel Pentium-J3710\nDDR4 4GB/ HDD 1000GB\nNo DVD/ kbd/ USBmouse \nFreeDos\nRUS (4XJ29EA) (без монитора)'
    m1 = InputTextMessageContent(
        message_text=text1 
    )
    result1 = InlineQueryResultArticle(
        title='HP 460-a210ur MicroTower',
        input_message_content=m1,
        description='120$',
        id=1
    )
    results = [result1]
    update.inline_query.answer(results)
def hp(update,context):
    text1='HP 460-a210ur MicroTower (SUS) \nIntel Pentium-J3710\nDDR4 4GB/ HDD 1000GB\nNo DVD/ kbd/ USBmouse \nFreeDos\nRUS (4XJ29EA) (без монитора)'
    text2='HP 290 G2 MicroTower (I5M)\nIntel Pentium-G5400\nDDR4 4GB/ HDD 1000GB\nNo DVD/ kbd/ USBmouse \nLCD 21,5" HP (3WP71AA) \nFreeDos\nRUS (5JP16ES)'
    text3='HP Desktop Pro G2 MicroTower (111/112)\nIntel i3 - 8100\nDDR4 4GB\nHDD 500GB/ DVD\nkbd/ USBmouse \nбез монитора \nFreeDos\nRUS (5QL16EA)'
    text4='HP 290 G2 MicroTower (SP2) \nCore i3-8100/ DDR4 4GB\nHDD 1TB/ DVD-RW\nLCD HP N246v 23.8"\nDOS /RUS (4YV34ES)'
    text5='HP 290 G2 MicroTower (8RY) \nIntel i5-8500\nDDR4 4GB/ HDD 500GB\nDVD\nkbd/ USBmouse \nLCD HP 24" N246v \nFreeDos\nRUS (4YV42ES)'
    text6='HP Omen Obelisk 875-0011ur (3ii)\nIntel i5-8500\nDDR4 8GB/HDD 1TB\nGeForce 1060 3GB\nWi-Fi/keyboard+mouse\nBT\nWin10\nJet Black (4UE94EA) No Monitor'
    text7='HP Omen 880-192ur (X5M) \nCore i7-9700K\nDDR4 16GB/ HDD 1TB\n256GB SSD\nNVIDIA GeForce GTX 2070 8GB/noDVD\nWin 10\nBlack (3QZ80EA) No Monitor'
    m1 = InputTextMessageContent(
        message_text=text1 
    )
    result1 = InlineQueryResultArticle(
        title='HP 460-a210ur MicroTower (SUS)\nIntel Pentium-J3710',
        input_message_content=m1,
        description='120$',
        id=1
    )
    m2 = InputTextMessageContent(
        message_text=text2 
    )
    result2 = InlineQueryResultArticle(
        title='HP 290 G2 MicroTower (I5M)\nIntel Pentium-G5400',
        input_message_content=m2,
        description='130$',
        id=2
    )
    m3 = InputTextMessageContent(
        message_text=text3 
    )
    result3 = InlineQueryResultArticle(
        title='HP Desktop Pro G2 MicroTower (111/112)\nIntel i3 - 8100',
        input_message_content=m3,
        description='140$',
        id=3
    )
    m4 = InputTextMessageContent(
        message_text=text4 
    )
    result4 = InlineQueryResultArticle(
        title='HP 290 G2 MicroTower (SP2)\nCore i3-8100',
        input_message_content=m4,
        description='165$',
        id=4
    )
    m5 = InputTextMessageContent(
        message_text=text5 
    )
    result5 = InlineQueryResultArticle(
        title='HP 290 G2 MicroTower (8RY)\nIntel i5-8500',
        input_message_content=m5,
        description='180$',
        id=5
    )
    m6 = InputTextMessageContent(
        message_text=text6 
    )
    result6 = InlineQueryResultArticle(
        title='HP Omen Obelisk 875-0011ur (3ii)\nIntel i5-8500',
        input_message_content=m6,
        description='200$',
        id=6
    )
    m7 = InputTextMessageContent(
        message_text=text7 
    )
    result7 = InlineQueryResultArticle(
        title='HP Omen 880-192ur (X5M)\nCore i7-9700K',
        input_message_content=m7,
        description='220$',
        id=7
    )
    results = [result1,result2,result3,result4,result5,result6,result7]
    update.inline_query.answer(results)
def legion(update,context):
    text = 'Legion C530-19ICB Personal Computer\nIntel i5-8400\nDDR4 16GB\nHDD 1000GB\nVGA 4GB Nvidia GTX 1050TI\nNo DVD\nNo kbd\nNo Monitor'
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='Legion C530-19ICB Personal Computer\nIntel i5-8400',
        input_message_content=m,
        description='190$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)
def zotac(update,context):
    text='Zotac G1107TK700B-U MEK1 Gaming\nIntel Core i7-7700\n16GB DDR4 RAM\n240GB NVMe SSD\n1TB HDD/ Video GeForce GTX 1070 Ti\nkeyboard\nmmouse\nWindows 10'
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='Zotac G1107TK700B-U MEK1 Gaming\nIntel Core i7-7700',
        input_message_content=m,
        description='250$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)
def notebook(update,context):
    asus = InlineKeyboardButton(text='Asus',switch_inline_query_current_chat='asus')
    lenovo = InlineKeyboardButton(text='Lenovo',switch_inline_query_current_chat='lenovo')
    acer = InlineKeyboardButton(text='Acer',switch_inline_query_current_chat='acer')
    hp = InlineKeyboardButton(text='HP',switch_inline_query_current_chat='HP')
    
    reply_markup = InlineKeyboardMarkup(
        [
            [asus,lenovo],
            [acer,hp]
        ]
    )
    update.message.reply_text(text='Notebooks 💻:',reply_markup=reply_markup)

def asus(update,context):
    text='ASUS X540M\nCeleron 4000\nDDR4 4GB\n500GB HDD\n15.6" HD LED\nUMA\nNo DVD\nRUS (без ОС)'
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='ASUS X540M\nCeleron 4000',
        input_message_content=m,
        description='258$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)
def lenovo(update,context):
    text='Lenovo Ideapad L340 \nIntel i3-8145U\nDDR4 4 GB\nHDD 1000GB \n15.6" HD TN\n2GB NVIDIA GeForce MX110\nNo DVD\nRUS (81LG007URK)'
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='Lenovo Ideapad L340 \nIntel i3-8145U',
        input_message_content=m,
        description='445$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)
def acer(update,context):
    text='Acer Extensa 2519\nCeleron 3060\nDDR3 4 GB\n500GB HDD\n15.6" HD LED\nUMA/ DVD \nRUS (NX.EFAER.122)'
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='Acer Extensa 2519\nCeleron 3060',
        input_message_content=m,
        description='250$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)
def HP(update,context):
    text='HP 15-rb028ur (385/136) \nAMD Dual-Core A4-9120\nDDR3 4 GB\nHDD 500GB\n15.6" HD LED\nAMD Radeon R3 integrated\nNo DVD \nRUS (4US49EA)'
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='HP 15-rb028ur (385/136) \nAMD Dual-Core A4-9120',
        input_message_content=m,
        description='242$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)

def Interfaoldoska(update,context):
    tanlash = InlineKeyboardButton(text='Tanlash',switch_inline_query_current_chat='tanlash1')
    reply_markup = InlineKeyboardMarkup(
        [
            [tanlash]
        ]
    )
    update.message.reply_text(text='Interfaol doska tanlash:',reply_markup=reply_markup)
def tanlash1(update,context):
    text='''"Интерактивная доска FPB 10 points 82"" interactive whiteboard  PH82\nФормат: 4:3, Активная поверхность доски: 1648x1176мм, Сенсорная технология: оптическая, Разрешение: 32768*32768, Время отклика: 10мс, Управление: 10 touch, \nстилус,пальцы или другие непрозрачные предметы, Материал доски: стальная поверхность, Интерфейс: USB 2.0, USB 3.0"'''
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='Интерактивная доска FPB 10 points 82',
        input_message_content=m,
        description='$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)

def Interaktivdispley(update,context):
    tanlash = InlineKeyboardButton(text='Tanlash',switch_inline_query_current_chat='tanlash2')
    reply_markup = InlineKeyboardMarkup(
        [
            [tanlash]
        ]
    )
    update.message.reply_text(text='Interfaol doska tanlash:',reply_markup=reply_markup)
def tanlash2(update,context):
    text='''"Интерактивная сенсорная панель FPB 65”\nДиагональ – 65”, Количество касаний – 10 (палец, перо или любые другие непрозрачные объекты), Активный размер - 1428x803мм, Соотношение сторон – 16:9, \nЯркость – 450cd/m2, Контраст – 5000:1, Подсветка – LED, Угол обзора – 178x178, Разрешение – 3840 х 2160 UHD 4K, Стерео система – 2x10W, Процессор – Intel Core i5-6400 2.7Ghz, \nОперативная память – 8GB, Жёсткий диск – SSD 240GB, Сеть – Gigabyte lan, Wi-Fi, Порты - HDMI, USB, VGA, audio, RJ-45"'''
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='Интерактивная сенсорная панель FPB 65',
        input_message_content=m,
        description='-',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)

def monoblok(update,context):
    hp = InlineKeyboardButton(text='HP',switch_inline_query_current_chat='monoblokhp')
    lenovo = InlineKeyboardButton(text='Lenovo',switch_inline_query_current_chat='lenovomonoblok')
    reply_markup = InlineKeyboardMarkup(
        [
            [hp,lenovo]
        ]
    )
    update.message.reply_text(text='Monoblok 💻:',reply_markup=reply_markup)

def hpmonoblok(update,context):
    text='HP ProOne 440 G4 (2QW) (Intel Pentium G5400T\nDDR4 8GB\nHDD 1000GB + SSD 128GB\nIntel UHD Graphics 630\n DVD/FHD 23,8" (1920 x 1080)\nkey + mouse) (5JP19ES)'
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='HP ProOne 440 G4 (2QW) (Intel Pentium G5400T',
        input_message_content=m,
        description='$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)
def lenovomonoblok(update,context):
    text='Lenovo IdeaCentre AIO V530-24ICB  (Intel i5-8400T\nDDR4 8GB/ HDD 1000GB \n23,8 FHD (1920x1080)\nIntel HD Graphics 630\nDVD-RW/ Wi-Fi \nkeyboard + mouse) Black (10UW000ARU)'
    m = InputTextMessageContent(
        message_text=text 
    )
    result = InlineQueryResultArticle(
        title='Lenovo IdeaCentre AIO V530-24ICB  (Intel i5-8400T',
        input_message_content=m,
        description='$',
        id=1
    )
    results = [result]
    update.inline_query.answer(results)



def qismlar(update,context0):
    protsessor = InlineKeyboardButton(text='Protsessor', switch_inline_query_current_chat='Protsessor')
    Materinskayaplata = InlineKeyboardButton(text='Materinskaya plata', switch_inline_query_current_chat='Materinskaya plata')
    Videokarta = InlineKeyboardButton(text='Video karta', switch_inline_query_current_chat='Video karta')
    Qattiqdisk = InlineKeyboardButton(text='Qattiq disk', callback_data='Qattiqdisk')
    DVD = InlineKeyboardButton(text='DVD', switch_inline_query_current_chat='DVD')
    OZU = InlineKeyboardButton(text='OZU', switch_inline_query_current_chat='OZU')
    Case = InlineKeyboardButton(text='Case', switch_inline_query_current_chat='Case')
    Blokpitanie = InlineKeyboardButton(text='Blok pitanie', switch_inline_query_current_chat='Blok pitanie')
    Coolers = InlineKeyboardButton(text='Coolers', switch_inline_query_current_chat='Coolers')

    reply_markup = InlineKeyboardMarkup(
        [
            [Qattiqdisk],
            [protsessor,Materinskayaplata],
            [Videokarta,DVD],
            [OZU,Case],
            [Blokpitanie,Coolers]
        ]
    )
    update.message.reply_text(text = 'Extiyot qismlari:\n',reply_markup=reply_markup)
#def Qattiqdisk(update,context):


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Extiyot qismlar ⚙️'),qismlar))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Kompyuter(pc) 🖥'),kompyuter))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Notebook 💻'),notebook))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Interfaol doska'),Interfaoldoska))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Interaktiv displey'),Interaktivdispley))
updater.dispatcher.add_handler(MessageHandler(Filters.text('Monoblok'),monoblok))

updater.dispatcher.add_handler(InlineQueryHandler(hp,pattern='hp'))
updater.dispatcher.add_handler(InlineQueryHandler(legion,pattern='legion'))
updater.dispatcher.add_handler(InlineQueryHandler(zotac,pattern='zotac'))

updater.dispatcher.add_handler(InlineQueryHandler(asus,pattern='asus'))
updater.dispatcher.add_handler(InlineQueryHandler(lenovo,pattern='lenovo'))
updater.dispatcher.add_handler(InlineQueryHandler(acer,pattern='acer'))
updater.dispatcher.add_handler(InlineQueryHandler(HP,pattern='HP'))

updater.dispatcher.add_handler(InlineQueryHandler(tanlash1,pattern='tanlash1'))
updater.dispatcher.add_handler(InlineQueryHandler(tanlash1,pattern='tanlash2'))

updater.dispatcher.add_handler(InlineQueryHandler(tanlash1,pattern='monoblokhp'))
updater.dispatcher.add_handler(InlineQueryHandler(lenovomonoblok,pattern='lenovomonoblok'))

#updater.dispatcher.add_handler(InlineQueryHandler(qattiqdisk,pattern='Qattiqdisk'))

updater.start_polling()
updater.idle()