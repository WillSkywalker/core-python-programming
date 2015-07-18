#!usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Unit 16

import socket

HOST = 'localhost'# raw_input('Address: ')
PORT = 21569
BUFSIZ = 4096
ADDR = (HOST, PORT)




while True:
    tcpCliSock = socket.socket(socket.AF_INET, 
                       socket.SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    data = raw_input('> ')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
    tcpCliSock.close()

# if __name__ == '__main__':
#     tcpCliSock = socket.socket(socket.AF_INET, 
#                                socket.SOCK_STREAM)
#     tcpCliSock.connect(ADDR)

#     print 'connected to', ADDR[0]
#     tcpCliSock.send('GET /zone/about.htm HTTP/1.0\r\nHost: %s\n' % HOST)
#     fhand = open('fromweb.htm', 'w+')
#     while True:
#         data = tcpCliSock.recv(BUFSIZ)
#         print 'receiving data...'
#         if not data:
#             break
#         print data
#         fhand.write(data)
