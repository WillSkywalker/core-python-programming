#!usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Unit 16
# import socket
from SocketServer import (TCPServer as TCP,
    StreamRequestHandler as SRH,
    BaseRequestHandler as BRH,
    UDPServer as UDP)
from time import ctime, sleep
import os

HOST = ''
PORT = 21569
BUFSIZ = 1024
ADDR = (HOST, PORT)


# tcpSerSock = socket.socket(socket.AF_INET, 
#                            # socket.SOCK_STREAM)
#                             socket.SOCK_DGRAM)
# tcpSerSock.bind(ADDR)
# # tcpSerSock.listen(5)

# while True:
#     print 'waiting for connection...'
#     # tcpClliSock, addr = tcpSerSock.accept()
#     # print '...connected from: ', addr

#     while True:
#         data, attr = tcpSerSock.recvfrom(BUFSIZ)
#         if not data:
#             break
#         tcpSerSock.send('[%s] %s' % (ctime(), data))

#     # tcpClliSock.close()

# tcpSerSock.close()


class MyRequestHandler(SRH):
    def handle(self):
        print '...connected from:', self.client_address
        # print self.connection
        inside = self.request.recv(BUFSIZ).rstrip()
        if inside.rstrip() == 'date':
            result = ctime()
        elif inside.rstrip() == 'os':
            result = os.name
        elif inside.startswith('ls'):
            result = os.listdir(os.curdir)
        elif inside.rstrip() == 'rest':
            sleep(5)
            result = '(Waited 5 sec) ' + inside
        else:
            result = inside

        self.request.send('[%s] %s' \
                             % (ctime(), result))
        
tcpServ = TCP(ADDR, MyRequestHandler)
print 'waiting for connection...'
tcpServ.serve_forever()
