class rxpsocket:
    @staticmethod
    def __init__(self, addressFamily, socketKind):


    def bind(self, address):

    def listen(self, [backlog]):
    def connect(self, address):
    def accept(self):
        # conn is a new socket object usable to send and
        # receive data on the connection, and address
        # is the address bound to the socket on the other
        # end of the connection
        return (conn, address)
    def send(self, bytes[, flags]):
    def recv(self, buffsize[, flags]):
    def close(self):
