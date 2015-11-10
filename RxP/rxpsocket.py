import random
import RxPException
from RxP.rxprotocol import rxprotocol

class rxpsocket:

    def __init__(self, proxy_addr=('127.0.0.1', 13000)):
        self.__proxy_addr = proxy_addr
        self.__port_num = None
        self.__ip_addr = '127.0.0.1' # TODO: ponder whether this is necessary


    def get_ip_addr(self):
        return self.__ip_addr

    def get_port_num(self):
        return self.__port_num

    def bind(self, address):
        if self.__port_num is None:
            self.__port_num = address[1]
            if not rxprotocol.register(self):
                self.__port_num = None
                raise RxPException(106)
        else:
            raise RxPException(105)

        # self.__ip_addr = '127.0.0.1' if len(address[0]) == 0 else address[0]
        # if address[1] != :
        #
        # is_registered = False
        # while not is_registered:
        #     is_registered = rxprotocol.register(self, address)

    def listen(self, max_num_queued):
        if self.__port_num is None:
            self.__assign_random_port(self)
        # TODO: this is not done

    def connect(self, address):
         if self.__port_num is None:
             self.__assign_random_port(self)
         # TODO: this is not done

    def __assign_random_port(self):
        count = 65536
        is_registered = False
        while count > 0 or not is_registered:
            self.__port_num = random.randrange(0, 65536)
            is_registered = rxprotocol.register(self)
            if not is_registered:
                self.__port_num = None
            count -= 1
        if not is_registered:
            raise RxPException(106)

    def accept(self):
        # conn is a new socket object usable to send and
        # receive data on the connection, and address
        # is the address bound to the socket on the other
        # end of the connection
        return (conn, address)

    def send(self, bytes[, flags]):

    def recv(self, buffsize[, flags]):
    
    def close(self):
