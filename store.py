from abstract_class import Storage


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
                print('Товар добавлен!')
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
