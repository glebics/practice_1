class Server():
    def __init__(self):
        self.buffer = []  # сюда будем хранить Data для отправления
        self.received_messages = []

    def send_data(self, data, server_ip):
        self.buffer.append(Data(data, server_ip))

    def get_data(self, data):
        self.received_messages.append(data)
        return self.received_messages

    def get_messages(self):
        return self.buffer

    def set_ip(self, ip):  # назначать ip адрес должен роутер,
        self.ip = ip       # у сервера есть только мак адрес по дефолту
        # (тут он не нужен), а неееет, по заданию должен при создании сервера
        # сделаю как в реальности, изменить легко будет

    def get_ip(self):
        return self.ip


class Router():
    def __init__(self):
        self.buffer = []  # сюда будем хранить сервера

    def link(self, server):
        self.buffer.append(server)
        server.set_ip(len(self.buffer))

    def unlink(self, server):
        self.buffer.remove(server)

    def get_buffer(self):
        return self.buffer

    def send_data(self):
        for server in self.buffer:
            server.get_messages()
            for data in server.get_messages():
                if data.ip == server.get_ip():
                    server.get_data(data)
                server.buffer.remove(data)


class Data():
    def __init__(self, data, ip):
        self.data = data
        self.ip = ip
    
    def __str__(self):
        return self.data


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

msg_lst_from = sv_from.get_messages()
msg_lst_to = sv_to.get_messages()

print(msg_lst_from)
print(msg_lst_to)
