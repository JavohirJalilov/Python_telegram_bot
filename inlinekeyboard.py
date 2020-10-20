from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import os

TOKEN = os.environ['echo']


def start(update, context):

    button1 = InlineKeyboardButton(
        text='👍🏻0',
        callback_data=1
    )
    inlinekeybord = InlineKeyboardMarkup(
        [
            [button1]
        ]
    )
    bot = context.bot
    chat_id = update.message.chat.id 
    bot.sendMessage(
        chat_id=chat_id,
        text = 'Siz dasturlashga qiziqasizmi!:0',
        reply_markup=inlinekeybord
    )

def help_bot(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    bot.sendMessage(chat_id, 'This is just echo bot.')


def inline(update,context):

    query = update.callback_query
    text = query.message.text

    count = ''
    for i in text:
        if i.isdigit():
            count += i

    count = int(count)
    count += 1
    print(count)

    button1 = InlineKeyboardButton(
        text=f'👍🏻{count}',
        callback_data=1
    )
    inlinekeybord = InlineKeyboardMarkup(
        [
            [button1]
        ]
    )
    

    query.edit_message_text(f'Siz dasturlashga qiziqasizmi!:{count}', reply_markup=inlinekeybord)
    data = query.data
    query.answer(' Good ! ')


updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('help', help_bot))
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(inline))

updater.start_polling()
updater.idle()