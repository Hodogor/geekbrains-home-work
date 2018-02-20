import select
import socket
import time

class Process:
    def __init__(self, address: str, port: int, blocking: int):
        self._is_sending_time = True
        socket_ = self.make_tcp_socket(address, port, blocking)
        method = self.send_time if blocking == 1 else self.send_time_non_blocking
        try:
            method(socket_)
        except KeyboardInterrupt:
            _is_sending_time = False
            socket_.close()
            print('Correctly closing')

    def make_tcp_socket(self, address: str, port: int, blocking: int) -> socket.socket:
        """ Создание TCP соединения"""
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Создает сокет TCP
        socket_.setblocking(blocking) 
        socket_.bind((address, port)) # Присваивает порт и адрес
        socket_.listen(5) #обслуживает не более 5 запросов
        print("Создан сокет")
        return socket_


    def send_time(self, socket_: socket.socket) -> None:
        """ Функция отправит время клиенту"""
        while self._is_sending_time:
            client, address = socket_.accept()
            print('Connected client from {}'.format(address))
            payload = time.ctime(time.time()) + '\n'
            client.send(payload.encode('ascii'))
            client.close()


    def send_time_non_blocking(self, socket_: socket.socket) -> None:
        """ отправка времени без блокировки"""
        while self._is_sending_time:
            is_ready = select.select((socket_,), tuple(), tuple(), 1)
            if not is_ready[0]:
                print('Not ready')
                continue
    
            client, address = socket_.accept()
            print('Connected client from {}'.format(address))
            payload = time.ctime(time.time()) + '\n'
            client.send(payload.encode('ascii'))
            client.close()


        
if __name__ == '__main__':
    proc = Process('', 8888, 1)
