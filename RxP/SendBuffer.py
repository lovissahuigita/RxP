class SendBuffer:

    __init__(self, initSeqNum):
        # lastByteSent - lastByteAcked <= min(receiveWindow, congestionWindow)
        __initialSequenceNumber     = initSeqNum
        __lastByteSent              =
        __lastByteAcked             =

        # this function need to have call back function, which will be called
        # when the timer ran out...
        __cb_startRestransmitTimer  =

        # this information will be taken from latest packet from processControlPacket()
        __receiveWindow             =
        __congestionWindow          =


    #need a queue as a buffer


    # put data from user space into buffer
    def put(self, data):

    def sendSegments(self):

    # return number of packet sent but not yet ACK'd by receiver
    def getNotReceivedCount(self):

    def processControlPacket(self, ctrlPacket): # to process FRR and ACK packets

    def setStartRestrasmitTimerCallBack(self, cb_startRestransmitTimer):




