import collections  # missing packet,     out of order packet

# duplicate packet
#
from FxA.util import util


class RecvBuffer:
    __logger = util.setup_logger()

    def __init__(self, buffer_size=int(1024)):
        self.__recv_buffer = collections.deque(maxlen=buffer_size)
        self.__recv_last_ackd = None;
        self.__recv_base = None;

        self.__send_buffer = collections.deque()
        self.__send_ackd_buffer = collections.deque()
        self.__send_base = None

    def getWindowSize(self):
        return self.__receive_buffer.maxlen - len(self.__receive_buffer)

    def recv_put(self, inboundPacket):
        expected_seq = self.__recv_base + len(self.__recv_base)
        if self.__recv_base is None:
            self.__recv_base = inboundPacket.get_seq_num
        if inboundPacket.get_seq_num() == expected_seq:
            if inboundPacket.get_data is not None:
                for data_byte in inboundPacket.get_data:
                    if len(self.__recv_buffer) < self.__recv_buffer.maxlen:
                        self.__recv_buffer.append(data_byte)
                    else:
                        self.__logger.info('recv buffer size: ' + len(
                            self.__recv_buffer) + '/' +
                                           self.__recv_buffer.maxlen
                                           + ' dropping segment seq# ' +
                                           inboundPacket.get_seq_num)
            if inboundPacket.get_ack:
                if self.__recv_last_ackd < inboundPacket.get_ack_num:
                    self.__recv_last_ackd = inboundPacket.get_ack_num
                if inboundPacket.get_yo:
                    # TODO: notify socket of YO!+ACK
                    pass
            elif inboundPacket.get_yo:
                # TODO: notify socket of YO!
                pass
            elif inboundPacket.get_cya:
                # TODO: notify socket of CYA
                pass



        else:
            self.__logger.info(' unexpected packet: expected seq#: ' +
                               expected_seq + ' received seq#:  ' +
                               inboundPacket.get_seq_num)

    def recv_take(self, max):
        pass
