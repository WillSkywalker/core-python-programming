#!usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Unit 16

from twisted.internet import protocol, reactor

HOST = 'localhost'
PORT = 21567
# BUFSIZ = 1024
# ADDR = (HOST, PORT)


class TSClntProtocol(protocol.Protocol):
    def sendData(self):
        data = raw_input('> ')
        if data:
            print '...sending %s...' % data
            self.transport.write(data)
        else:
            self.transport.lostConnection()

    def connectionMade(self):
        self.sendData()

    def dataReceived(self, data):
        print data
        self.sendData()


class TSClntFactory(protocol.ClientFactory):
    protocol = TSClntProtocol
    clientConnectionLost = clientConnectionFailed = \
        lambda self, connector, reason: reactor.stop()


if __name__ == '__main__':
    reactor.connectTCP(HOST, PORT, TSClntFactory())
    reactor.run()
        
        
