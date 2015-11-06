import argparse
import logging

# set up logger
logger = logging.getLogger('debug')
logHandler = logging.StreamHandler()
logFormatter = logging.Formatter(
    '[%(asctime)s] %(levelname)s/%(funcName)s/%('
    'lineno)d: '
    '%(message)s')
logHandler.setFormatter(logFormatter)
logger.addHandler(logHandler)


def main():
    parser = argparse.ArgumentParser(description='Parse command-line '
                                                 'arguments')
    parser.add_argument('X', type=int, help='port number at which the '
                                            'FxA-client’s UDP socket should '
                                            'bind to (even number), this port '
                                            'number should be equal to the '
                                            'server’s port number minus 1');
    parser.add_argument('A', type=str, help='the IP address of NetEmu')
    parser.add_argument('P', type=int, help='UDP port number of NetEmu')

    # action store_true to make the the args.verbose == false if not specified
    parser.add_argument('-v', '--verbose', help='print out process '
                                                'messages',
                        action='store_true')
    args = parser.parse_args()
    if args.verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.ERROR)
    logger.debug("hello")


if __name__ == "__main__":
    main()
