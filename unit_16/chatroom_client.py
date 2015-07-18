#!usr/bin/env python
# Author: Will Skywalker

# Core Python Programming - Unit 16

import sys, socket, select

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST, PORT)

username = raw_input('Your name: ')
tcpCliSock = socket.socket(socket.AF_INET, 
                       socket.SOCK_STREAM)
tcpCliSock.connect(ADDR)


while True:
    targets = [sys.stdin, tcpCliSock]
    read_sockets, write_sockets, error_sockets = \
        select.select(targets, [], [])

    for sock in read_sockets:
        if sock == tcpCliSock:
            data = sock.recv(BUFSIZ)
            if not data:
                print 'Connection lost!'
                sys.exit()
            print data
        else:
            message = raw_input('> ')
            tcpCliSock.send(username+': '+message)