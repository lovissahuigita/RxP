from socket import socket, AF_INET, SOCK_DGRAM

class Connection:
    __AVAIL_STATE = ["", ""] # list of all states

    def __init__(self):
        __netSocket = socket(AF_INET, SOCK_DGRAM)
        __netSocket.bind(address)
        __state =

    def getState(self):
    def initHandshake
    def initTearDown
    def getInitialSequenceNumber:    # this will be random
    def discoverMTU:                 # Look: PMTUD algorithm

