import argparse
import logging
import re
import traceback

from FxA.RxPException import RxPException
from FxA.sock import sock
from FxA.util import util, ArgumentCountException

__logger = None
__portNum = None
__ne_addr = None
__socket = None


def main():
    parser = setup_cl_parser()
    args = parser.parse_args()

    # need to redeclare to write to global vars
    global __portNum
    global __ne_addr
    global __socket
    global __logger

    __logger = util.setup_logger()
    if args.verbose:
        __logger.setLevel(logging.DEBUG)
    else:
        __logger.setLevel(logging.ERROR)
    __portNum, __ne_addr = util.parse_args(args.X, args.A, args.P)
    if __portNum % 2 == 1:
        util.exit_error('X has to be even number')

    newsocketbind()
    help_message()
    prompt_user_command()


def newsocketbind():
    try:
        global __socket
        __socket = sock(__ne_addr)
        __socket.bind(('', __portNum))
    except RxPException as err:
        util.exit_error(str(err))


def help_message():
    print('Type \'help\' for list of command, \'exit\' to quit.')


def command_conn(*_):
    __logger.info('running command \'connect\'')
    __logger.debug('connecting to ' + str(('127.0.0.1', __portNum + 1)))

    try:
        connected = False
        while not connected:
            try:
                __logger.debug('attempting to make connection')
                __socket.connect(('127.0.0.1', __portNum + 1))
                connected = True
            except RxPException as err:
                if err.errno() == 103:
                    __logger.debug(
                        'existing socket was closed, making a new one')
                    newsocketbind()
                else:
                    raise
    except RxPException as err:
        print(util.ERROR_TAG + str(err))
    except OSError:
        __logger.debug('\n' + traceback.format_exc())
        print(util.ERROR_TAG + 'unable to make connection')


def command_get(F):
    __logger.info('running command \'get\'')

    try:
        if len(F) == 0:
            __logger.debug(str(F))
            raise ArgumentCountException('get', 1, 'F')
        util.send_msg('GET ' + F, __socket)
        F = re.split('/', F)
        F = 'cfile/' + F[len(F) - 1]
        util.download(__socket, F)
    except RxPException as err:
        print(util.ERROR_TAG + str(err))
    except ArgumentCountException as err:
        print(util.ERROR_TAG + str(err))
    except OSError:
        __logger.debug('\n' + traceback.format_exc())
        print(util.ERROR_TAG + 'please run \'connect\' command first.')


def command_post(F):
    __logger.info('running command \'post\'')

    try:
        if len(F) == 0:
            __logger.debug(str(F))
            raise ArgumentCountException('post', 1, 'F')
        sF = re.split('/', F)
        sF = 'sfile/' + sF[len(sF) - 1]
        util.send_msg('POST ' + sF, __socket)
        util.upload(__socket, F)
    except RxPException as err:
        print(util.ERROR_TAG + str(err))
    except ArgumentCountException as err:
        print(util.ERROR_TAG + str(err))
    except OSError:
        __logger.debug('\n' + traceback.format_exc())
        print(util.ERROR_TAG + 'please run \'connect\' command first.')


# need review
def command_wind(W):
    __logger.info('running command \'window\'')
    try:
        if len(W) == 0:
            raise ArgumentCountException('window', 1, ('W'))
        __socket.set_buffer_size(int(W))
    except ArgumentCountException as err:
        print(util.ERROR_TAG + str(err))


def command_disconn(*_):
    __logger.info('running command \'disconnect\'')
    try:
        __logger.debug('trying to disconnect existing connection')
        __socket.close()
        print('Please wait at least 240s (TIME_WAIT) before connecting with '
              'the same socket.')
    except OSError:
        __logger.debug('\n' + traceback.format_exc())
        print(util.ERROR_TAG + 'please run \'connect\' command first.')


def command_help(*_):
    __logger.info('running command \'help\'')
    print('Commands:')
    print('\tconnect\t\tconnects to the FxA-server (running at the same IP '
          'host)')
    print('\tget F\t\tdownloads \'F\' from the server')
    print('\tpost F\t\tuploads \'F\' to the server')
    print('\twindow W\tconfigure maximum receiver window size for the '
          'client (in segments)')
    print('\tdisconnect\tterminates gracefully from the FxA-server')
    print('\thelp\t\tprint this help message')
    print('\texit\t\texit this program (this is ungraceful close)')


def command_exit(*_):
    __logger.info('running command \'exit\'')
    exit()


__command_dict = {
    'connect'   : command_conn,
    'get'       : command_get,
    'post'      : command_post,
    'window'    : command_wind,
    'disconnect': command_disconn,
    'help'      : command_help,
    'exit'      : command_exit
}


def prompt_user_command():
    while True:
        user_input = re.split('\s+', input('FxA client > ').strip(),
                              maxsplit=1)
        __logger.debug(str(user_input))
        if user_input[0] in __command_dict:
            __command_dict.get(user_input[0])(
                user_input[1] if len(user_input) > 1 else '')
        else:
            print(util.ERROR_TAG + 'Invalid command \'' + str(user_input[0])
                  + '\'')
            help_message()


def setup_cl_parser():
    parser = argparse.ArgumentParser(description='Parse command-line '
                                                 'arguments')
    parser.add_argument('X', type=int, help='port number at which the '
                                            'FxA-client’s UDP socket '
                                            'should bind to (even number), '
                                            'this port number should be '
                                            'equal to the '
                                            'server’s port number minus 1')
    parser.add_argument('A', type=str, help='the IP address of NetEmu')
    parser.add_argument('P', type=int, help='UDP port number of NetEmu')

    # action store_true to make the the args.verbose == false if not specified
    parser.add_argument('-v', '--verbose', help='print out process messages',
                        action='store_true')
    return parser


if __name__ == "__main__":
    main()
