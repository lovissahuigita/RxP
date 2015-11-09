class RxPException(Exception):
    # Form -> errno: errmsg
    ERROR = {
        100: 'Port number in use (cannot bind error).',
        101: 'Connection refused (no listening socket exists).',
        102: 'Not connected (no connection error).',
        103: 'Socket already closed.',
        104: 'Socket is already connected.',
        105: 'Socket already bound.',
        106: 'Socket is in use.',
        107: 'Connection force closed by peer.',
        108: ''
    }

    def __init__(self, errno):
        self.__errno = errno
        self.__msg = self.ERROR.get(errno)

    def msg(self):
        return self.__msg

    def errno(self):
        return self.__errno

    def __str__(self):
        return str(self.__errno) + ' ' + self.__msg
