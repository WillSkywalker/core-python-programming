#!usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Unit 16
import socket, select
# from SocketServer import (TCPServer as TCP,
#     StreamRequestHandler as SRH)
from time import ctime
import os

HOST = ''
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)


tcpSerSock = socket.socket(socket.AF_INET, 
                           socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

CLIENTS = [tcpSerSock]
data = ''

while True:
    try:
        # print 'waiting for connection...'
        read_sockets,write_sockets,error_sockets = \
            select.select(CLIENTS,[],[])

        for sock in read_sockets:
            if sock == tcpSerSock:
                tcpClliSock, addr = tcpSerSock.accept()
                print '...connected from:', addr
                CLIENTS.append(tcpClliSock)
            else:
                data = sock.recv(BUFSIZ)
                for each in CLIENTS:
                    if each not in (tcpSerSock, sock):
                        each.send(data)

              
        # tcpClliSock.close()
    except KeyboardInterrupt:
        tcpSerSock.close()
        break



        
# tcpServ = TCP(ADDR, MyRequestHandler)
# print 'waiting for people joining...'
# tcpServ.serve_forever()
