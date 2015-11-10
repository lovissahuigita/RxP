class Packet:
    # class attributes here
    
    def __init__(self):
        # instance attributes here
        __sourcePort 	    =
        __destinationPort   =
        __sequenceNumber	=
        __ackNumber	        =

        # number of packet to be retransmitted starting at seqNum ACK
        # maybe should be as big as window size
        __frrAmount         =
        __recvWindowSize 	=
        __checksum	        =

        # ACK, HI, BYE, RST, FRR (Fast Retransmit Request)
        __typeBits	        =
        __data		        =






