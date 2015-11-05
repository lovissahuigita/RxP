class RecvBuffer:

    __init__(self):
        # receiveWindow = receiveBuffer.size - (lastByteRcvd - lastByteRead)
        __lastByteRead      =
        __lastByteRcvd      =       # not necessarily in order
        __cb_send           =
        __cb_startAckTimer  =

    # need a queue as a buffer

    def getWindowSize(self):

    # put incoming received packet to buffer
    # will also check for duplicate packet, and reorder packet if necessary
    def buffer(self, inboundPacket):
        # if inboundPacket is out of order / there are missing packet,
        #   send fast retransmit request message (using cb_send)
        #   as soon as all received packet is ordered, send cumulative ack

    # copy and remove the oldest received packet to user space
    def take(self):
        return #something

    # return number received but not yet ACK'd
    def getUnACKdCount(self):

    # return first missing packet seqnum
    def getMissingPacketSeqNum(self):

    # set callback function for sending packet
    def setSendCallBack(self, cb_send):

    def setStartAckTimerCallBack(self, cb_startAckTimer):


