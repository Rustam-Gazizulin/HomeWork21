


class Store(Storage):

    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                print('Товар добавлен')
                self.__items[name] += count
                return True
            else:
                if isinstance(self, Shop):
                    print('Недостаточно места в магазине!')
                elif isinstance(self, Store):
                    print('Недостаточно места на складе!')
                return False
        else:
            if self.get_free_space() >= count:
                print('Товар добавле!')
                self.__items[name] = count
                return True
            else:
                if isinstance(self, Shop):
                    print('Недостаточно места в магазине!')
                elif isinstance(self, Store):
                    print('Недостаточно места на складе!')
                return False

    def remove(self, name, count):
        if self.__items[name] >= count:
            print('Нужное количество есть на складе!')
            self.__items[name] -= count
            return True
        else:
            print('Недостаточно места на складе!')
            return False

    def get_free_space(self):
        current_space = 0
        for value in self.__items.values():
            current_space += value
        return self.__capacity - current_space

    def get_items(self):
        return self.__items

    def get_unique_items_count(self):
        return len(self.__items.keys())

    def __str__(self):
        st = ''
        for key, value in self.__items.items():
            st += f'{key}: {value}\n'
        return st


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() >= 5:
            print('Лимит превышен')
            return False
        else:
            super().add(name, count)


class Request:
    def __init__(self, request_str):
        req_list = request_str.split()
        action = req_list[0]
        self.__count = int(req_list[1])
        self.__item = req_list[2]
        if action == 'Доставить':
            self.__from = req_list[4]
            self.__to = req_list[6]
        elif action == 'Забрать':
            self.__from = req_list[4]
            self.__to = None
        elif action == 'Привезти':
            self.__from = req_list[4]
            self.__to = None

    def move(self):
        if self.__to and self.__from:
            if eval(self.__to).add(self.__item, self.__count):
                eval(self.__from).remove(self.__item, self.__count)

        elif self.__to:
            eval(self.__to).add(self.__item, self.__count)
        elif self.__from:
            eval(self.__from).remove(self.__item, self.__count)


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
