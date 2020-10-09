import telegram
import random

bot = telegram.Bot(token='1391772239:AAFuxhKB5Fu1uKIbzAP_bZFpJhseNeacCXk')

def Tabrik():
    str_t = [
        
        {
            1:'''Tug`ilgan kuningiz bilan  Javohir ! Barcha ezgu maqsadlaringiz ro`yobga chiqsin! Baxtli va oilaviy farovonlik xamda omad qushi xamisha yo`ldosh bo`lsin!''',

            2:'''Sizga oilaviy tinchlik, sixat-salomatlik va ruxiy tetiklik tilayman. Xayotdan zavqlanib yashash nasib etsin! Tug`ilgan kuningiz bilan!''',

            3:'''Tavallud ayomingiz bilan! Xayotingiz to`kin-sochin bo‘lsin, barcha maqsadlaringiz ro`yobga chiqsin. Baxtli, tinch-totuv va dorilomon xayot xamisha yo`ldosh bo`lsin''',

            4:'''Tug`ilgan kuningiz bilan! Mustaxkam sog`lik, kuch-qudrat va omad xamda baxt, yaxshi kayfiyat doimiy xamroxingizga aylansin! Farovon turmush kechirish baxti nasib etsin!'''

        }
    ]
    return str_t

def birthday():
    getUpdates = bot.getUpdates()[-1]
    
    birth = Tabrik()
    list_new = []
    for value in birth[0].values():
        list_new.append(value)

    return random.sample(list_new,k=1)   


last_update_id = -1

while True:
    getUpdates = bot.getUpdates()[-1]
    chat_id = getUpdates.message.chat.id
    update_id = getUpdates.update_id
    text = getUpdates.message.text

    print(f'last: {last_update_id} = id: {update_id}')

    if last_update_id != update_id:

        if text =='/start':
            bot.sendMessage(chat_id=chat_id,text='Tabriklash uchun ism kiriting:')
        else:
            s = text+" "+birthday()[0]
            bot.sendMessage(chat_id=chat_id,text=s)

        last_update_id = update_id
