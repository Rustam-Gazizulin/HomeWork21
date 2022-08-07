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
            if super().add(self.__item, self.__count):
                super().remove(self.__item, self.__count)

        elif self.__to:
            eval(self.__to).add(self.__item, self.__count)
        elif self.__from:
            eval(self.__from).remove(self.__item, self.__count)
