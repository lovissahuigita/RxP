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

    # generate checksum for given data
    def __computeChecksum(cls, data)

    # validate data integrity
    def validateChecksum()

    # breakdown data into packets
    def packetize

    # create a selective retransmit request to the sender
    def makeFastRetransmitPacket(ackNum)

    def makeHiPacket(self, srcPort, destPort, seqNum = 0):





