import logging
import re
import sys


class util(object):
    __util_logger = None

    @classmethod
    def setup_logger(cls):
        if cls.__util_logger is None:
            cls.__util_logger = logging.getLogger('debug')
            log_handler = logging.StreamHandler()
            log_formatter = logging.Formatter(
                '[%(asctime)s] %(levelname)s/%(funcName)s/%(lineno)d: '
                '%(message)s')
            log_handler.setFormatter(log_formatter)
            cls.__util_logger.addHandler(log_handler)
        cls.__util_logger.info("logger set up!")
        return cls.__util_logger

    @staticmethod
    def exit_error(msg):
        print('[ERROR] ' + msg, file=sys.stderr)
        exit()

    @classmethod
    def parse_args(cls, port_num, ne_ip, ne_port):
        cls.__util_logger.info(
            'NetEmu: ' + str(ne_ip) + ':' + str(ne_port) + ' client port: ' +
            str(port_num))
        try:
            port_num = int(port_num)
            if (port_num < 0) or (port_num > 65535):
                raise PortNumberInvalid
        except ValueError:
            cls.exit_error(str(port_num) + ' is not a number!')
        except PortNumberInvalid:
            cls.exit_error(str(port_num) + ' is not in valid port number '
                                           'range')
        except:
            raise

        try:
            ip_pattern = re.compile(
                '(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})')
            match = ip_pattern.match(ne_ip)
            if match:
                for octet in match.groups():
                    byte = int(octet)
                    if byte < 0 or byte > 255:
                        raise InvalidIP4Format
            else:
                raise InvalidIP4Format

            ne_port = int(ne_port)
            if ne_port < 0 or ne_port > 65535:
                raise PortNumberInvalid
        except ValueError:
            cls.exit_error(str(ne_port) + ' is not a number!')
        except InvalidIP4Format:
            cls.exit_error(str(ne_ip) + ' is not a valid IPv4 format')
        except PortNumberInvalid:
            cls.exit_error(str(ne_port) + ' is not in valid port number range')
        except:
            raise
        return port_num, (ne_ip, ne_port)


class PortNumberInvalid(Exception):
    pass


class InvalidIP4Format(Exception):
    pass
