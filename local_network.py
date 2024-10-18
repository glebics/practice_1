from typing import List, Dict


class Data:
    def __init__(self, data: str, ip: int) -> None:
        """Инициализирует объект данных с содержимым и IP-адресом получателя."""
        self.data: str = data
        self.ip: int = ip

    def __str__(self) -> str:
        """Возвращает текст сообщения."""
        return self.data

    def __repr__(self) -> str:
        """Возвращает текст сообщения при отображении списка."""
        return f"'{self.data}'"
    
    def get_ip(self) -> int:
        """Возвращает IP-адрес получателя."""
        return self.ip


class Server:
    def __init__(self) -> None:
        """Инициализирует сервер с буфером для отправки и списком полученных сообщений."""
        self.buffer: List[Data] = []  # сюда будем хранить Data для отправления
        self.received_messages: List[Data] = []

    def send_data(self, data: str, server_ip: int) -> None:
        """Отправляет данные на указанный IP-адрес сервера."""
        self.buffer.append(Data(data, server_ip))

    def get_data(self) -> List[Data]:
        """Возвращает список полученных сообщений."""
        return self.received_messages

    def receive_data(self, data: Data) -> None:
        """Принимает данные и добавляет их в список полученных сообщений."""
        self.received_messages.append(data)

    def get_messages(self) -> List[Data]:
        """Возвращает буфер отправленных сообщений."""
        return self.buffer

    def set_ip(self, ip: int) -> None:
        """Устанавливает IP-адрес сервера."""
        self.ip: int = ip

    def get_ip(self) -> int:
        """Возвращает IP-адрес сервера."""
        return self.ip

    def __str__(self) -> str:
        """Возвращает IP-адрес сервера."""
        return f"Server IP: {self.ip}"


class Router:
    def __init__(self) -> None:
        """Инициализирует роутер с буфером серверов."""
        self.buffer: Dict[int, Server] = {}  # сюда будем хранить сервера

    def link(self, server: Server) -> None:
        """Подключает сервер к роутеру и назначает ему IP-адрес."""
        ip = len(self.buffer) + 1  # Генерируем IP-адрес
        server.set_ip(ip)
        self.buffer[ip] = server

    def unlink(self, server: Server) -> None:
        """Отключает сервер от роутера."""
        ip = server.get_ip()
        if ip in self.buffer:
            del self.buffer[ip]

    def get_buffer(self) -> Dict[int, Server]:
        """Возвращает список подключенных серверов."""
        return self.buffer

    def send_data(self) -> None:
        """Отправляет данные от серверов к их получателям."""
        for server in self.buffer.values():
            messages = server.get_messages()
            for data in messages:
                if data.get_ip() in self.buffer:
                    self.buffer[data.get_ip()].receive_data(data)
                server.buffer.remove(data)

    def __str__(self) -> str:
        """Возвращает количество подключенных серверов."""
        return f"Router with {len(self.buffer)} servers connected"


#   исполняемый код
router = Router()
sv_from = Server()
sv_from2 = Server()

router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())

assert len(router.get_buffer()) == 4, "должно быть 4 сервера в буфере"

sv_to = Server()
router.link(sv_to)

sv_from.send_data("Hello", sv_to.get_ip())
sv_from.send_data("Hello 2", sv_from2.get_ip())
sv_from2.send_data("Hello", sv_to.get_ip())
sv_to.send_data("Hi", sv_from.get_ip())

msg_lst_from = sv_from.get_messages()
msg_lst_to = sv_to.get_messages()

print(msg_lst_from)
print(msg_lst_to)

router.send_data()
assert len(router.get_buffer()) == 5, "должно быть 5 серверов в буфере"

msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()

print(msg_lst_from)
print(msg_lst_to)
