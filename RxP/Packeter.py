#__author__ = 'lovissa'

class Packeter:

    MSS = 544 # in bytes

    # breakdown data into packets
    #  input data is already in binary 
    # this method breaks the binary to 544 bytes def
    @classmethod
    def packetize(cls, data):
        packetList = []
        bytearrsize = len(data)
        leftover = bytearrsize

        while leftover > 0:
            if leftover >= cls.MSS:
                newPacket =
                packetList.append(newPacket)
                leftover -= len(newPacket)
            else:  
                leftover =  
        return packetList 


    # generate checksum for given data
    def __computeChecksum(cls, data):

    # validate data integrity
    def validateChecksum():

    # create a selective retransmit request to the sender
    def makeFastRetransmitPacket(ackNum):

    def makeHiPacket(self, srcPort, destPort, seqNum = 0):