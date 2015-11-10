class Packet:
    # class attributes here
    
    def __init__(self, src_port, dst_port, seq_num, ack_num, data):
        # instance attributes here
        self.__src_port = src_port
        self.__dst_port = dst_port
        self.__seq_num = seq_num
        self.__ack_num = ack_num

        # number of packet to be retransmitted starting at seqNum ACK
        # maybe should be as big as window size
        self.__recv_window_size = 0
        self.__checksum	= 0

        # ACK, HI, BYE, RST, FRR (Fast Retransmit Request)
        self.__yo = False
        self.__cya = False
        self.__ack_number = 0
        self.__data = data

    def set_checksum(self, checksum):
        self.__checksum = checksum

    def get_checksum(self):
        return self.__checksum

    def set_yo(self):
        self.__yo = True

    def set_cya(self):
        self.__cya = True