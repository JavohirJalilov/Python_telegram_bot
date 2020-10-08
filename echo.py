import telegram

bot = telegram.Bot(token='1302971549:AAGx9wgPHvKZQtLpV29iMkmqGZTPqR6UQeE')

last_update_id = -1

while True:
    getUpdates = bot.getUpdates()[-1]
    chat_id = getUpdates.message.chat.id
    text = getUpdates.message.text
    update_id = getUpdates.update_id

    print(f'last: {last_update_id} = id: {update_id}')
    if last_update_id != update_id:
        if text == '/start':
            bot.sendMessage(chat_id = chat_id, text = 'marhamt')
        else:
            bot.sendMessage(chat_id = chat_id, text = text)

        last_update_id = update_id