from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler,InlineQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResult,InlineQueryResultArticle,InputTextMessageContent

import os

TOKEN = os.environ['TOKEN']


def start(update, context):

    button = InlineKeyboardButton(
        text='search',
        switch_inline_query_current_chat='search'
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
        text='Search programming language',
        reply_markup=reply_markup
    )


def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')

list1=[]
list2=[]

def inlinequery(update,context):
    query = update.inline_query.query
    print(query)
    mess = InputTextMessageContent(
        message_text='text'
    )
    result1 = InlineQueryResultArticle(
        title='python',
        input_message_content=mess,
        thumb_url='https://thecode.media/wp-content/uploads/2019/05/2-1-1080x718.jpg',
        id=1
    )
    result2 = InlineQueryResultArticle(
        title='Java Script',
        input_message_content=mess,
        thumb_url='https://cdn4.iconfinder.com/data/icons/scripting-and-programming-languages/512/js-512.png',
        id=2
    )
    
    results = [result1,result2]
    update.inline_query.answer(results)

updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(InlineQueryHandler(callback=inlinequery))
updater.start_polling()
updater.idle()