coffe_1 = 'shirin'
coffe_2 = 'achchiq'

name = input('ismingiz: ')
sorov = input('Coffee ichasizmi: ')

if sorov == 'ha' or sorov == 'Ha' or sorov == 'Ha albatta':
    coffee_tur = input(f'{name} qanday coffee ichasiz: ')
    if coffee_tur == coffe_1 or coffee_tur == coffe_2:
        if coffee_tur == coffe_1:
            print(f'{name} sizning {coffe_1} coffe buyurtmangizni 5 minutda tayyorlab beramiz !')
        else:
            print(f'{name} sizning {coffe_2} coffe buyurtmangizni 5 minutda tayyorlab beramiz !')
    else:
        print(f'{name}, kechirasiz bizda bunday turdagi coffee mavjud emas.')
else:
    print(f'Kechirasiz, {name} biz faqat coffee tayyorlaymiz.')