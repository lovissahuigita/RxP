import argparse
import logging
import re

from FxA.sock import sock
from FxA.util import util

__logger = None
__ne_addr = None
__portNum = None
__socket = None


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
    global __ne_addr
    global __socket
    __portNum, __ne_addr = util.parse_args(args.X, args.A, args.P)
    __socket = sock()
    __socket.bind(('', __portNum))
    help_message()
    prompt_user_command()


def command_conn(*_):
    __logger.info('running command \'connect\'')
    __socket.connect(__ne_addr)


def command_get(F):
    __logger.info('running command \'get\'')
    pass


def command_post(F):
    __logger.info('running command \'post\'')
    pass


def command_wind(W):
    __logger.info('running command \'window\'')
    pass


def command_disconn(*_):
    __logger.info('running command \'disconnect\'')
    pass


def command_help(*_):
    __logger.info('running command \'help\'')
    pass


def command_exit(*_):
    __logger.info('running command \'exit\'')
    exit()


def help_message():
    print('Type \'help\' for list of command, \'exit\' to quit.')


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
        user_input = re.split('\s+', input('FxA client > '), maxsplit=1)
        __logger.debug(str(user_input))
        if user_input[0] in __command_dict:
            __command_dict.get(user_input[0])(
                user_input[1] if len(user_input) > 1 else None)
        else:
            print('Invalid command \'' + str(user_input[0]) + '\'')
            help_message()


def setup_cl_parser():
    parser = argparse.ArgumentParser(description='Parse command-line '
                                                     'arguments')
    parser.add_argument('X', type=int, help='port number at which the '
                                                'FxA-client’s UDP socket '
                                                'should '
                                                'bind to (even number), '
                                                'this port '
                                                'number should be equal to '
                                                'the '
                                                'server’s port number minus '
                                                '1');
    parser.add_argument('A', type=str, help='the IP address of NetEmu')
    parser.add_argument('P', type=int, help='UDP port number of NetEmu')

    # action store_true to make the the args.verbose == false if not specified
    parser.add_argument('-v', '--verbose', help='print out process '
                                                    'messages',
                            action='store_true')
    return parser


if __name__ == "__main__":
    main()
