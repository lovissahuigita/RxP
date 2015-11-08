# socket wrapper
import socket
from _socket import SHUT_WR

from FxA.RxPException import RxPException


class sock:
    def __init__(self, proxy_addr = ('127.0.0.1', 13000)):
        self.__addr = None
        try:
            self.__s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except:
            raise

    def connect(self, address):
        try:
            self.__s.connect(address)
        except OSError as err:
            if err.winerror == 10038:
                raise RxPException(103)
            elif err.winerror == 10056:
                raise RxPException(104)
            elif err.winerror == 10048:
                raise RxPException(106)
            else:
                print(self.__s)
                raise
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
            return self.__s.send(dataBytes)
        except OSError as err:
            if int(err.winerror) == 10057:
                raise RxPException(102)
            else:
                raise

    def recv(self, maxBytesRead):
        try:
            # mesg, senderAddr = self.__s.recvfrom(maxBytesRead)
            # if senderAddr is self.__addr:
            #     raise Exception
            # else:
            #     return mesg
            return self.__s.recv(maxBytesRead)
        except:
            raise

    # set receive buffer size to x segment
    def set_buffer_size(x):
        pass

    def close(self):
        try:
            print(str(self.__s))
            self.__s.shutdown(SHUT_WR)
            self.__s.close()
        except:
            raise

    def __str__(self):
        return str(self.__s)

    def __repr__(self):
        return str(self.__s)
