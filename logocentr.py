from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def add(self, name, count):
        pass

    @abstractmethod
    def remove(self, name, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):

    def __init__(self, items: dict, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def add(self, name, count):
        if name in self.__items.keys():
            if self.get_free_space() >= count:
                self.__items[name] += count
            else:
                print('Недостаточно места')
                return 'Insufficient_space'
        else:
            if self.get_free_space() >= count:
                self.__items[name] = count
            else:
                print("ываываы")
                return 'Insufficient_space'

    def remove(self, name, count):
        if self.__items[name] > count:
            self.__items[name] -= count
        else:
            print('Недостаточно места')
            return 'Not enough product in stock'

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
            return 'The limit of unique products has been exceeded!'
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
            self.__from = req_list[6]
            self.__to = None

    def move(self):
        if self.__to:
            self.__to.add(self.__item, self.__count)
        if self.__from:
            self.__from.remove(self.__item, self.__count)

# storage1 = Shop(items={'iphone': 5, 'xiaomi': 5, 'xiaomi1': 5, 'xiaomi2': 2, 'xiaomi3': 1})
#
# storage1.add('tablet', 3)
# print(storage1)
# print(storage1.get_free_space())

# storage1.remove('xiaomi', 10)
# print(storage1.get_free_space())
# print(storage1.get_items())
# print(storage1.get_unique_items_count())
# print(storage1)
