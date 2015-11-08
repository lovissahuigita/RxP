# socket wrapper
import socket


class sock:
    def __init__(self):
        try:
            self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            raise

    def connect(self, address):
        try:
            self.__s.connect(address)
        except:
            raise

    def bind(self, address):
        try:
            self.__s.bind(address)
        except:
            raise

    def listen(self, maxQC):
        try:
            self.__s.listen(maxQC)
        except:
            raise

    def accept(self):
        try:
            return self.__s.accept()
        except:
            raise


def send(self, dataBytes):
    try:
        self.__s.send(dataBytes)
    except:
        raise


def recv(self, maxBytesRead):
    try:
        return self.__s.recv(maxBytesRead)
    except:
        raise


def close(self):
    try:
        self.__s.close()
    except:
        raise


def __str__(self):
    return str(self.__s)


def __repr__(self):
    return str(self.__s)
