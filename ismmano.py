import telegram
import requests

bot = telegram.Bot(token='1391772239:AAFuxhKB5Fu1uKIbzAP_bZFpJhseNeacCXk')

last_update_id = -1

while True:
    getUpdates = bot.getUpdates()[-1]
    chat_id = getUpdates.message.chat.id
    update_id = getUpdates.update_id
    text = getUpdates.message.text

    print(f'last: {last_update_id} = id: {update_id}')
    if last_update_id != update_id:

        res = requests.get(f'https://ismlar.com/search/{text}')
        s = res.text
    
        x = s.index('class="mb-3"')
        y = s.index('</h3>',x)

        x += 111 + len(text)
        tur = s[x:y]

        if text == '/start':
            mano = 'Marhamt! Ismni kiriting.'
            bot.sendMessage(chat_id=chat_id,text=mano) 

        elif tur == 'Исм маъносини топиш учун буюртма бериш':
            mano = 'Afsus, Bunday ism hozircha birda mavjud emas'
            bot.sendMessage(chat_id=chat_id,text=mano) 

        else:
            i = s.index('class="text-size-5"')
            l = s.index('</p>',i)
            i = i+20

            k = s.index('class="fas fa-tag"')
            j = s.index('</a>',k)
            k+=23
            tur = s[k:j]

            mano = s[i:l]
            bot.sendMessage(chat_id=chat_id,text=tur+'\n'+mano) 
        last_update_id = update_id