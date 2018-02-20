import socket

class Socket_client:
    def __init__(self, address='', port=8888):
        socket_ = self.make_tcp_socket(address, port)
        self.recive_time(socket_)

    def make_tcp_socket(self, address: str = 'localhost',
                        port: int = 8888) -> socket.socket:
        """ Подключить клиент к серверу"""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((address, port))
        return s
    
    
    def recive_time(self, socket_: socket.socket) -> None:
        """ Получить время от сервера"""
        payload = socket_.recv(1024)
        socket_.close()
        print('Received time is {}'.format(payload.decode('ascii')))


pr = Socket_client('localhost')
input()
