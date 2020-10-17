# A very simple Flask Hello World app for you to get started with...
import telegram
from flask import Flask
from flask import request,jsonify
from telegram.ext import CommandHandler, Dispatcher, Filters, MessageHandler
from queue import Queue


TOKEN = '1324065101:AAGdpyczF0dAbFl35PK9KwhTLo9W6Fs-FwA'
bot = telegram.Bot(TOKEN)

app = Flask(__name__)

@app.route('/getInfo')
def getInfo():

    info = bot.getWebhookInfo()
    return info.to_json()

@app.route('/set')
def setWebhook():
    HOOK_URL = 'https://motof.pythonanywhere.com'
    hook_bool = bot.setWebhook(url=HOOK_URL)
    return str(hook_bool)

@app.route('/getMe')
def getMe():
    user = bot.getMe()
    return user.to_json()



def start(update, context):
    print('Replt_text')
    update.message.reply_text('hi')


def hi(update, context):
    bot = context.bot
    text = update.message.text
    chat_id = update.message.chat.id
    # bot.sendMessage(chat_id, text)
    update.message.reply_text(text)

@app.route('/',methods=['POST'])
def main():

    dp = Dispatcher(bot,None,workers=0)

    if request.method == "POST":
        print('POST')
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dp.add_handler(CommandHandler('start',start))
        dp.add_handler(MessageHandler(Filters.text, hi))

        dp.process_update(update)




    return 'ok'