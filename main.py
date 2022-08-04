from logocentr import Shop, Store, Request

print('Hello!')

storage_1 = Store(items={'iphone': 5, 'xiaomi': 10, 'oneplus': 15, 'samsung': 5, 'oppo': 5, 'asus': 1})
storage_2 = Store(items={'iphone': 10, 'xiaomi': 20, 'oneplus': 30, 'samsung': 10})
shop_1 = Shop(items={'iphone': 5, 'xiaomi': 10})

# while True:
#     user_text = input('Enter the command:\n')
#
#     if user_text == 'stop':
#         break
#
#     else:
#         req = Request(user_text)
#         req.move()

test_text = 'Доставить 3 xiaomi из склад shop_1'
req = Request(test_text)
req.move()

