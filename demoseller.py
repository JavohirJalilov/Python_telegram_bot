from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,InlineQueryHandler,CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup,ReplyKeyboardMarkup,ReplyMarkup,KeyboardButton,InputTextMessageContent,InlineQueryResultArticle,KeyboardButton
import telegram

import os

TOKEN = os.environ['demo']
dic = {}
lis = []
def Help(update,context):
    text = 'This is just Demo seller bot.!'
    bot = context.bot 
    Catalog = KeyboardButton(text='🏬 Catalog')
    Orders = KeyboardButton(text='📦 Orders')
    Userinfo = KeyboardButton(text='👤 Userinfo')
    Cart = KeyboardButton(text='🛒 Cart')
    Administration = KeyboardButton(text='🎛 Administration')
    
    keyboard = ReplyKeyboardMarkup(
        [
            [Catalog,Orders],
            [Userinfo,Cart],
            [Administration]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text=text,reply_markup=keyboard) 

def start(update,context):
    text = 'Hello! 👋 \nThis is a demo version of the Telegram Store bot. You can test out catalog function and checkout process.'
    bot = context.bot 
    Catalog = KeyboardButton(text='🏬 Catalog')
    Orders = KeyboardButton(text='📦 Orders')
    Userinfo = KeyboardButton(text='👤 Userinfo')
    Cart = KeyboardButton(text='🛒 Cart')
    Administration = KeyboardButton(text='🎛 Administration')
    
    keyboard = ReplyKeyboardMarkup(
        [
            [Catalog,Orders],
            [Userinfo,Cart],
            [Administration]
        ],
        resize_keyboard=True
    )
    update.message.reply_text(text=text,reply_markup=keyboard) 
def catalog(update,context):
    print(1)
    query = update.callback_query
    catalog = InlineKeyboardButton(
        text='🍕 pizza',
        switch_inline_query_current_chat='🍕 pizza'
    )
    reply_markup = InlineKeyboardMarkup(
        [
            [catalog]
        ]
    )
    update.message.reply_text(text='🏬 Catalog',reply_markup=reply_markup)
def catalogquery(update,context):
    query = update.inline_query.query
    print(query)
    button = InlineKeyboardButton(text='➕ Add to card',callback_data='addcard')
    keyboard=InlineKeyboardMarkup([[button]])
    text='\n$22\.99\n\nOriginal Signature crust, 100% whole milk mozzarella, Canadian\-style bacon, applewood smoked bacon, sliced red onions, Dole® pineapple chunks, Kogi™ Serrano Chili sauce drizzle, and topped with fresh chopped cilantro\.'
    url='https://c1.tchpt.com/admin/aux?b=c1~4066c4e45b62c35f92d362574ab3a0c91&a=c1~576&f=KogiSerranoChili_1024x768__2019-07-30_17-33-45.jpg'
    mes = InputTextMessageContent(
        message_text=f'[Chili Pizza \(14"\)]({url}){text}',
        parse_mode='MarkdownV2',
    )
    result1 = InlineQueryResultArticle(
        title='Chili Pizza (14")',
        input_message_content=mes,
        thumb_url=url,
        id=1,
        description='$22.99',
        reply_markup=keyboard
    )
    results = [result1]
    update.inline_query.answer(results)
def userinfo(update,context):
    bot = context.bot
    query = update.callback_query
    chat_id = update.message.chat.id
    first_name = update.message.from_user.first_name
    
    adresses = InlineKeyboardButton(
        text='🗺 addresses',
        callback_data='addresses'
    )
    adress = InlineKeyboardButton(
        text='➕Add address',
        callback_data='addaddress'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [adresses,adress]
        ]
    )
    text = f'👤 {first_name}\n🤝 Invited friends: 0\n💸 Bonus balance: $0.0\nℹ️ You can get 5.0% on your bonus balance from the amount of each order of your invited friends.'
    bot.sendMessage(chat_id,text=text,reply_markup=keyboard)
def administration(update,context):
    Users = KeyboardButton(text='👥 Users')
    Orders = KeyboardButton(text='🏷 Orders')
    Welcome = KeyboardButton(text='👋 Welcome text')
    Bonus = KeyboardButton(text='🤑 Bonus rate')
    Add = KeyboardButton(text='➕ Add category')
    Remove = KeyboardButton(text='🗑 Remove category')
    New = KeyboardButton(text='📦 New product')
    Delete = KeyboardButton(text='🗑 Delete product')
    Exit = KeyboardButton(text='🚪 Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [Users,Orders],
            [Welcome,Bonus],
            [Add,Remove],
            [New,Delete],
            [Exit]
        ],
        resize_keyboard=True
    )
    text = update.message.text
    update.message.reply_text(text,reply_markup=keyboard)
def newbonus(update,context):
    Cancel = KeyboardButton(text='❌ Cancel')
    keyboard = ReplyKeyboardMarkup(
        [
            [Cancel]
        ],
        resize_keyboard=True
    )
    text = update.message.text
    update.message.reply_text(text,reply_markup=keyboard)
def noavailable(update,context):
    Users = KeyboardButton(text='👥 Users')
    Orders = KeyboardButton(text='🏷 Orders')
    Welcome = KeyboardButton(text='👋 Welcome text')
    Bonus = KeyboardButton(text='🤑 Bonus rate')
    Add = KeyboardButton(text='➕ Add category')
    Remove = KeyboardButton(text='🗑 Remove category')
    New = KeyboardButton(text='📦 New product')
    Delete = KeyboardButton(text='🗑 Delete product')
    Exit = KeyboardButton(text='🚪 Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [Users,Orders],
            [Welcome,Bonus],
            [Add,Remove],
            [New,Delete],
            [Exit]
        ],
        resize_keyboard=True
    )
    text = '⚡️ Not available in demo version.'
    update.message.reply_text(text,reply_markup=keyboard)
def welcometext(update,context):
    welcome = KeyboardButton(text='❌ Cancel')
    keyboard = ReplyKeyboardMarkup(
        [
            [welcome]
        ],
        resize_keyboard=True
    )
    text='👋 New welcome text\nSend the text of greeting in one message.\nYou can use Telegram Markdown to format your message:\n*bold text* _italic text_'
    update.message.reply_text(text,reply_markup=keyboard)
def cart(update,context):
    clear = InlineKeyboardButton(
        text='❌ Clear',
        callback_data='clear'
    )
    placeorder = InlineKeyboardButton(
        text='✅ Place order',
        callback_data='plaseorder'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [clear,placeorder]
        ]
    )
    text='🛒 Cart\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n💵 Total: $22.99'
    update.message.reply_text(text,reply_markup=keyboard)

def clear(update,context):
    query = update.callback_query 
    query.edit_message_text('✅ Cart cleared')
    query.answer(text='Working...')
def plaseorder(update,context):
    bot = context.bot
    query = update.callback_query
    chat_id = update.callback_query.message.chat.id
    text = '📍 Choose shipping address:'
    addres = KeyboardButton(
        text = '📍 Address',
        request_location=True
    )
    cancel = KeyboardButton(text = '🚪 Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [addres],
            [cancel]
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text=text,reply_markup=keyboard)
    query.answer('Working...')
def order(update,context):
    calcel = InlineKeyboardButton(
        text='❌ Cancel',
        callback_data='cancel'
    )
    accept = InlineKeyboardButton(
        text='✅ Accept',
        callback_data='accept'
    )
    keyboard = InlineKeyboardMarkup(
        [
            [calcel,accept]
        ]
    )
    text='📦 Your order\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n💵 Amount to pay: $22.99\n\n💬 Comment to the order: 📦 Orders'
    update.message.reply_text(text,reply_markup=keyboard)
def addaddress(update,context):
    text ='📍 Please send the address to which you want your order to be delivered.'
    bot = context.bot 
    query = update.callback_query
    chat_id = update.callback_query.message.chat.id 
    bot.sendMessage(chat_id,text=text)
    query.answer(text='Working...')
#     bot = update.callback_query.bot
#     chat_id = query.message.chat.id
#     message_id = query.message.message_id
#     bot.delete_message(chat_id,message_id)
#     print(dir(bot))
def cancel(update,context):
    query = update.callback_query
    query.edit_message_text(text='❌ Order cancelled')
def accept(update,context):
    bot = context.bot
    query = update.callback_query
    text2='✅ Order placed!'
    text1 = '📦 Your order\n\nChili Pizza (14") - $22.99 x1 = $22.99\n\n💵 Amount to pay: $22.99\n\n💬 Comment to the order: 📦 Orders'
    chat_id = update.callback_query.message.chat.id
    query.edit_message_text(text=text1)
    bot.sendMessage(chat_id,text=text2)
def addresses(update,context):
    query = update.callback_query
    bot = context.bot
    chat_id = update.callback_query.message.chat.id
    text = ' Please send the address to which you want your order to be delivered.'
    location = KeyboardButton(
        text = '📍 Location',
        request_location=True
    )
    cancel = KeyboardButton(text = '🚪 Exit')
    keyboard = ReplyKeyboardMarkup(
        [
            [location],
            [cancel]
        ],
        resize_keyboard=True
    )
    bot.sendMessage(chat_id,text=text,reply_markup=keyboard)
    query.answer('Working...')

def addcard(update, context):
    query = update.callback_query
    query.answer(text='✅ Added to card')

def user(update,context):
    query = update.callback_query
    update.message.reply_text(text='No users')

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', Help))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🏬 Catalog'),catalog))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👤 Userinfo'),userinfo))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🎛 Administration'),administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🚪 Exit'),start))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🤑 Bonus rate'),newbonus))
updater.dispatcher.add_handler(MessageHandler(Filters.text('❌ Cancel'),administration))
updater.dispatcher.add_handler(MessageHandler(Filters.text('➕ Add category'),noavailable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Remove category'),noavailable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 New product'),noavailable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🗑 Delete product'),noavailable))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👋 Welcome text'),welcometext))
updater.dispatcher.add_handler(MessageHandler(Filters.text('🛒 Cart'),cart))
updater.dispatcher.add_handler(MessageHandler(Filters.text('📦 Orders'),order))
updater.dispatcher.add_handler(MessageHandler(Filters.text('👥 Users'),user))

updater.dispatcher.add_handler(InlineQueryHandler(catalogquery,pattern='🍕 pizza'))

updater.dispatcher.add_handler(CallbackQueryHandler(addcard,pattern='addcard'))
updater.dispatcher.add_handler(CallbackQueryHandler(cancel,pattern='cancel'))
updater.dispatcher.add_handler(CallbackQueryHandler(accept,pattern='accept'))
updater.dispatcher.add_handler(CallbackQueryHandler(clear,pattern='clear'))
updater.dispatcher.add_handler(CallbackQueryHandler(plaseorder,pattern='plaseorder'))
updater.dispatcher.add_handler(CallbackQueryHandler(addaddress,pattern='addaddress'))
updater.dispatcher.add_handler(CallbackQueryHandler(addresses,pattern='addresses'))

updater.start_polling()
updater.idle()