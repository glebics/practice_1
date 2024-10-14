class ObjList():
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def __next__(self):
        if not self.__next:
            raise StopIteration
        return self.__next

    def __prev__(self):
        if not self.__prev:
            raise StopIteration
        return self.__prev

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data):
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj


class LinkedList():
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__current = None

    def __iter__(self):
        self.__current = self.__head
        return self

    def __next__(self):
        if self.__current is None:
            raise StopIteration
        else:
            obj = self.__current
            self.__current = self.__current.get_next()
            return obj

    def add_obj(self, obj):
        if self.__head is None:
            self.__head = obj
            self.__tail = obj
        else:
            self.__tail.set_next(obj)
            obj.set_prev(self.__tail)
            self.__tail = obj

    def remove_obj(self):
        if self.__tail is None:
            return
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.get_prev()
            self.__tail.set_next(None)

    def get_data(self):
        if self.__head is None:
            return []
        else:
            data_set = []
            if self.__current is None:
                self.__current = self.__head
            for obj in self:
                data_set.append(obj.get_data())
            return data_set


#   исполняемый код
ob = ObjList("данные 1")
lst = LinkedList()
lst.add_obj(ob)
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))

res = lst.get_data()

print(res)  # ['данные 1', 'данные 2', 'данные 3']
