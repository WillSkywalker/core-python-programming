#!usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Unit 16

from twisted.internet import protocol, reactor
from time import ctime

PORT = 21567

# tcpSerSock = socket.socket(socket.AF_INET, 
                           # socket.SOCK_STREAM)
# tcpSerSock.bind(ADDR)
# tcpSerSock.listen(5)

# while True:
#     print 'waiting for connection...'
#     tcpClliSock, addr = tcpSerSock.accept()
#     print '...connected from: ', addr

#     while True:
#         data = tcpClliSock.recv(BUFSIZ)
#         if not data:
#             break
#         tcpClliSock.send('[%s] %s' % (ctime(), data))

#     tcpClliSock.close()

# tcpSerSock.close()


class TSServProtocol(protocol.Protocol):
    def connectionMade(self):
        clnt = self.clnt = self.transport.getPeer().host
        print '...connected from:', clnt

    def dataReceived(self, data):
        self.transport.write('[%s] %s' % (ctime(), data))
        
        
if __name__ == '__main__':
    factory = protocol.Factory()
    factory.protocol = TSServProtocol
    print 'waiting for connection...'
    reactor.listenTCP(PORT, factory)
    reactor.run()