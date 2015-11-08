import argparse
import logging
import re
from threading import Thread, Lock

from FxA.sock import sock
from FxA.util import util

__logger = None
__portNum = None
__socket = None
__serving_thread = None
__client_socket_lock = None
__client_list = {}


def main():
    parser = setup_cl_parser()
    args = parser.parse_args()

    global __logger
    __logger = util.setup_logger()
    if args.verbose:
        __logger.setLevel(logging.DEBUG)
    else:
        __logger.setLevel(logging.ERROR)

    # need to redeclare to write to global vars
    global __portNum
    global __socket
    global __serving_thread
    global __client_socket_lock
    __portNum, ne_addr = util.parse_args(args.X, args.A, args.P)
    if __portNum % 2 == 0:
        util.exit_error('X has to be odd number')
    __socket = sock(ne_addr)
    __socket.bind(('', __portNum))
    __socket.listen(65535)
    help_message()
    __client_socket_lock = Lock()
    __serving_thread = Thread(None, serve_client, 'client-server')
    __serving_thread.start()
    prompt_user_command()


def command_wind(W):
    __logger.info('running command \'window\'')
    __logger.info('acquiring socket_lock')
    __client_socket_lock.acquire()
    for cli_addr in __client_list:
        __client_list.get(cli_addr).set_buffer_size(int(W))
    __logger.info('releasing socket_lock')
    __client_socket_lock.release()


# this is still very very wrong need confirmation on what it does!
def command_term(*_):
    __logger.info('running command \'terminate\'')
    __logger.info('acquiring socket_lock')
    __client_socket_lock.acquire()
    for cli_addr in __client_list:
        __client_list.get(cli_addr).close()
        __logger.debug(str(__client_list.get(cli_addr)))
    __logger.info('releasing socket_lock')
    __client_socket_lock.release()


def command_help(*_):
    __logger.info('running command \'help\'')
    print('Commands:')
    print('\twindow W\t\tconfigure maximum receiver window size for the '
          'server (in segments)')
    print('\tterminate\t\tshut down FxA-Server gracefully')
    print('\thelp\t\t\tprint this help message')


def command_exit(*_):
    __logger.info('running command \'exit\'')
    exit()


def help_message():
    print('Type \'help\' for list of command, \'exit\' to quit.')


__command_dict = {
    'window'   : command_wind,
    'terminate': command_term,
    'help'     : command_help,
    'exit'     : command_exit
}


def client_post(client_sock, filename, *_):
    try:
        file = open(filename, 'wb')
        __logger.debug('Writing ' + filename)
        rcvd = client_sock.recv(4096)
        rcvdsize = int(len(rcvd))
        bytewritten = int(0)
        while len(rcvd) != 0:
            __logger.debug('Received ' + str(len(rcvd)) + ' bytes')
            while bytewritten < rcvdsize:
                bytewritten += file.write(rcvd)
                __logger.debug(
                    'Writting ' + str(bytewritten) + '/' + str(rcvdsize))
            rcvd = client_sock.recv(4096)
            rcvdsize += int(len(rcvd))
        file.close()
        __logger.debug('Wrote ' + str(bytewritten) + ' bytes')
    except:
        raise


def client_get(client_sock, filename, *_):
    try:
        bytesent = int(0)
        __logger.debug('Reading ' + filename)
        file = open(filename, 'rb')
        __logger.debug(str(file))
        data = file.read(1024)
        __logger.debug(str(data))
        filesize = int(len(data))
        while bytesent < filesize:
            __logger.debug('sent: ' + str(bytesent) + '/' + str(filesize))
            bytesent += client_sock.send(data)
            data = file.read(1024)
            filesize += int(len(data))
        __logger.debug('sent: ' + str(bytesent) + '/' + str(filesize))
        file.close()
    except:
        raise


__client_command_dict = {
    'POST': client_post,
    'GET' : client_get
}


def proccess_client(client_sock, msg):
    msg = re.split('\s+', msg, maxsplit=1)
    __logger.debug(str(msg))
    if msg[0] in __client_command_dict:
        __client_command_dict.get(msg[0])(client_sock, msg[1] if len(msg) > 1
        else None)
    else:
        pass


def serve_client():
    while True:
        __logger.info('acquiring socket_lock')
        __client_socket_lock.acquire()
        print('Waiting for client...')
        served_socket, client_addr = __socket.accept()
        __client_list[client_addr] = served_socket
        __logger.info('releasing socket_lock')
        __client_socket_lock.release()
        print('Serving ' + str(client_addr))
        msg = served_socket.recv(1024)
        while not (len(msg) == 0):
            decoded = msg.decode(util.TEXT_ENCODING)
            print(decoded)
            proccess_client(served_socket, decoded)
            msg = ''#served_socket.recv(1024)
        print('Finished serving ' + str(client_addr))
        print('Closing socket ' + str(served_socket))
        __logger.info('acquiring socket_lock')
        __client_socket_lock.acquire()
        __client_list.pop(client_addr)
        __logger.info('releasing socket_lock')
        __client_socket_lock.release()
        served_socket.close()


def prompt_user_command():
    while True:
        user_input = input('FxA client > ').strip()
        user_input = re.split('\s+', user_input, maxsplit=1)
        __logger.debug(str(user_input))
        if user_input[0] in __command_dict:
            __command_dict.get(user_input[0])(
                user_input[1] if len(user_input) > 1 else None)
        else:
            print(util.ERROR_TAG + 'Invalid command \'' + str(user_input[0])
                  + '\'')
            help_message()


def setup_cl_parser():
    parser = argparse.ArgumentParser(description='Parse command-line '
                                                 'arguments')
    parser.add_argument('X', type=int, help='port number at which the '
                                            'FxA-server’s UDP socket '
                                            'should '
                                            'bind to (odd number)');
    parser.add_argument('A', type=str, help='the IP address of NetEmu')
    parser.add_argument('P', type=int, help='UDP port number of NetEmu')

    # action store_true to make the the args.verbose == false if not specified
    parser.add_argument('-v', '--verbose', help='print out process messages',
                        action='store_true')
    return parser


if __name__ == "__main__":
    main()
