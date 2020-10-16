from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import os

TOKEN = os.environ['echo']


def start(update, context):

    button = InlineKeyboardButton(
        text='Like and Dislike',
        callback_data='like_dislike'
    )
    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button]
        ]
    )

    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(
        chat_id=chat_id,
        text='Like our bot!',
        reply_markup=reply_markup
    )


def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')

list1=[]
list2=[]
def inline1(update, context):
    callbackquery = update.callback_query.data
    if callbackquery=='like':
        list1.append('a')
    elif callbackquery=='dislike':
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

    reply_markup = InlineKeyboardMarkup(
        inline_keyboard=[
            [button1,button2]
        ]
    )

    query = update.callback_query
    text = query.message.text
    print(like,dislike)
    query.edit_message_text(f'thank you very much!', reply_markup=reply_markup)
    data = query.data
    query.answer(
        text='🤨😊😁😂',
        show_alert=True
    )


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(inline1))

updater.start_polling()
updater.idle()