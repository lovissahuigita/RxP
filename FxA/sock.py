# socket wrapper
import socket


class sock:
    def __init__(self):
        self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, address):
        self.__s.connect(address)

    def bind(self, address):
        self.__s.bind(address)

    def listen(self, maxQC):
        self.__s.listen(maxQC)

    def accept(self):
        return self.__s.accept()

    def send(self, dataBytes):
        self.__s.send(dataBytes)

    def recv(self, maxBytesRead):
        return self.__s.recv(maxBytesRead)

    def close(self):
        self.__s.close()
