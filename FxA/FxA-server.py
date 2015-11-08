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


def command_wind(W):
    __logger.info('running command \'window\'')
    pass


def command_term(*_):
    __logger.info('running command \'disconnect\'')
    pass


def command_help(*_):
    __logger.info('running command \'help\'')
    pass


def help_message():
    print('Type \'help\' for list of command.')


__command_dict = {
    'window'    : command_wind,
    'terminate': command_term,
    'help'      : command_help
}


def prompt_user_command():
    while True:
        user_input = re.split('\s+', input('FxA server > '), maxsplit=1)
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
