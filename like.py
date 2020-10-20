from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import os

TOKEN = os.environ['echo']

def start(update,context):

    button1 = InlineKeyboardButton(
        text='Like and Dislike',
        callback_data='like_dislike'
    )
    button2 = InlineKeyboardButton(
        text='Mobile and desctop',
        callback_data='Telegram_desctop'
    )
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button1,button2]
        ]
    )
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(
        chat_id=chat_id,
        text='Like, dislike and Mobile, desctop',
        reply_markup=reply_markup
    )

def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')

list1=[]
list2=[]
def like(update, context):
    query = update.callback_query
    callbackquery = update.callback_query.data
    if callbackquery=='like':
        list1.append('a')
    if callbackquery=='dislike':
        list2.append('b')
    like = len(list1)
    dislike = len(list2)

    button1 = InlineKeyboardButton(
        text=f'👍🏻 {like}',
        callback_data='like'
    )
    button2 = InlineKeyboardButton(
        text=f'👎🏻 {dislike}',
        callback_data='dislike'
    )
    button3 = InlineKeyboardButton(
        text = '🔙back',
        callback_data='back'
    )

    reply_markup = InlineKeyboardMarkup(
        [
            [button1,button2],
            [button3]
        ]
    )
    print(like,dislike)
    query.edit_message_text('thank you very much!',reply_markup=reply_markup)
    data = query.data
    query.answer(
        text='🤨😊😁😂'
    )

list3=[]
list4=[]
def mobile(update,context):
    query = update.callback_query
    callbackquery = update.callback_query.data
    if callbackquery=='mobile':
        list3.append('c')
    if callbackquery=='desctop':
        list4.append('d')
    mobile = len(list3)
    desctop = len(list4)

    button1 = InlineKeyboardButton(
        text=f'📱 {mobile}',
        callback_data='mobile'
    )
    button2 = InlineKeyboardButton(
        text=f'💻 {desctop}',
        callback_data='desctop'
    )
    button3 = InlineKeyboardButton(
        text = '🔙back',
        callback_data='back'
    )

    reply_markup = InlineKeyboardMarkup(
        [
            [button1,button2],
            [button3]
        ]
    )
    print(mobile,desctop)
    query.edit_message_text('Telegramga qaysi qurilmadan kirasiz?',reply_markup=reply_markup)
    data = query.data
    query.answer(
        text='🤨😊😁😂'
    )


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(like,pattern='like_dislike'))
updater.dispatcher.add_handler(CallbackQueryHandler(like,pattern='like'))
updater.dispatcher.add_handler(CallbackQueryHandler(like,pattern='dislike'))
updater.dispatcher.add_handler(CallbackQueryHandler(mobile,pattern='Telegram_desctop'))
updater.dispatcher.add_handler(CallbackQueryHandler(mobile,pattern='mobile'))
updater.dispatcher.add_handler(CallbackQueryHandler(mobile,pattern='desctop'))
updater.dispatcher.add_handler(CallbackQueryHandler(back,pattern='🔙back'))

updater.start_polling()
updater.idle()