from typing import Any, Optional


class ObjList:
    def __init__(self, data: Any):
        """Инициализирует узел ObjList с данными и без указателей на следующий или предыдущий узел."""
        self.__data: Any = data
        self.__next: Optional['ObjList'] = None
        self.__prev: Optional['ObjList'] = None

    def __next__(self) -> 'ObjList':
        """Возвращает следующий узел; вызывает StopIteration, если следующего узла нет."""
        if not self.__next:
            raise StopIteration
        return self.__next

    def __prev__(self) -> 'ObjList':
        """Возвращает предыдущий узел; вызывает StopIteration, если предыдущего узла нет."""
        if not self.__prev:
            raise StopIteration
        return self.__prev

    def get_data(self) -> Any:
        """Возвращает данные, хранящиеся в этом узле."""
        return self.__data

    def get_next(self) -> Optional['ObjList']:
        """Возвращает следующий узел."""
        return self.__next

    def get_prev(self) -> Optional['ObjList']:
        """Возвращает предыдущий узел."""
        return self.__prev

    def set_data(self, data: Any) -> None:
        """Устанавливает данные для этого узла."""
        self.__data = data

    def set_next(self, obj: 'ObjList') -> None:
        """Устанавливает следующий узел."""
        self.__next = obj

    def set_prev(self, obj: 'ObjList') -> None:
        """Устанавливает предыдущий узел."""
        self.__prev = obj


class LinkedList:
    def __init__(self):
        """Инициализирует пустой связный список."""
        self.__head: Optional[ObjList] = None
        self.__tail: Optional[ObjList] = None
        self.__current: Optional[ObjList] = None

    def __iter__(self) -> 'LinkedList':
        """Возвращает объект итератора (self) и сбрасывает текущий узел на головной."""
        self.__current = self.__head
        return self

    def __next__(self) -> ObjList:
        """Возвращает следующий узел списка при итерации."""
        if self.__current is None:
            raise StopIteration
        else:
            obj = self.__current
            self.__current = self.__current.get_next()
            return obj

    def add_obj(self, obj: ObjList) -> None:
        """Добавляет узел ObjList в конец связного списка."""
        if self.__head is None:
            self.__head = obj
            self.__tail = obj
        else:
            self.__tail.set_next(obj)
            obj.set_prev(self.__tail)
            self.__tail = obj

    def remove_obj(self) -> None:
        """Удаляет последний объект из связного списка."""
        if self.__tail is None:
            return
        if self.__head == self.__tail:
            self.__head = None
            self.__tail = None
        else:
            self.__tail = self.__tail.get_prev()
            if self.__tail:
                self.__tail.set_next(None)

    def get_data(self) -> list:
        """Возвращает список данных из всех узлов связного списка."""
        if self.__head is None:
            return []
        else:
            data_set = []
            if self.__current is None:
                self.__current = self.__head
            for obj in self:
                data_set.append(obj.get_data())
            return data_set


#   Исполняемый код
ob = ObjList("данные 1")
lst = LinkedList()
lst.add_obj(ob)
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))

res = lst.get_data()

print(res)  # ['данные 1', 'данные 2', 'данные 3']
