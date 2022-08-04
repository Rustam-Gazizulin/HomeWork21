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
        assortiment = ''
        for key, value in self.__items.items():
            assortiment += f'{key}: {value}\n'
        return assortiment


class Shop(Store):
    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, name, count):
        if self.get_unique_items_count() > 5:
            print('Лимит превышен')
            return 'The limit of unique products has been exceeded!'
        else:
            super().add(name, count)



storage1 = Shop(items={'iphone': 10, 'xiaomi': 6})

storage1.add('tablet', 4)
# print(storage1)
# print(storage1.get_free_space())

# storage1.remove('xiaomi', 10)
# print(storage1.get_free_space())
# print(storage1.get_items())
# print(storage1.get_unique_items_count())
# print(storage1)



