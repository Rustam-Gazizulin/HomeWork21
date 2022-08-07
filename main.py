from request import Request

from store import Store, Shop

storage_1 = Store(items={'iphone': 5, 'xiaomi': 10, 'oneplus': 15, 'samsung': 5, 'oppo': 5, 'asus': 1})
storage_2 = Store(items={'iphone': 10, 'xiaomi': 20, 'oneplus': 30, 'samsung': 10})
shop_1 = Shop(items={'iphone': 5, 'xiaomi': 10})

while True:
    print('Актуальные остатки на складе')
    print(f'{"-" * 10}\nstorage_1:\n{"-" * 10}\n{storage_1}')
    print(f'{"-" * 10}\nstorage_2:\n{"-" * 10}\n{storage_2}')
    print(f'{"-" * 10}\nshop_1:\n{"-" * 10}\n{shop_1}')
    user_text = input('Enter the command:\n')

    if user_text == 'stop':
        break

    else:
        try:
            req = Request(user_text)
            req.move()
        except Exception as e:
            print(f'Произошла ошибка {e}')

#  Доставить 5 xiaomi из storage_1 to storage_2
#  Забрать 3 xiaomi in shop_1
#  Привезти 3 xiaomi in shop_2
