#!/usr/bin/python

from socket import *

users = dict()

host = ''
port = 19940

sock = socket(AF_INET, SOCK_STREAM)

sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

sock.bind((host, port))

sock.listen(1)

while True:
    clntSock, clntAddr = sock.accept()
    clntFile = clntSock.makefile("r", 0)

    message = clntFile.readline().strip()

    action, username = message.split()

    if (action == "ENTER"):
        users[username] = clntSock

        print "{"
        for keys, values in users.items():
            print keys + ":", values
        print "}"
    elif (action == "EXIT"):
        users[username].close()
        del users[username]
        clntSock.close()

        print "{"
        for keys, values in users.items():
            print keys + ": ", values
        print "}"

    clntFile.close()
