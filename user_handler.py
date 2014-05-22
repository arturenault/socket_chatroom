#!/usr/bin/python

from socket import *
from signal import *
from multiprocessing.reduction import reduce_handle, rebuild_handle

host = ''
port = 19940
users = {}

def quit(signum, frame):
    for each in users:
        fd = rebuild_handle(users[each])
        quitSock = fromfd(fd, AF_INET, SOCK_STREAM)
        quitSock.send("Server terminated.")
        quitSock.close()
        del users[each]
    exit(0)

def dict_is_empty(d):
    try:
        for k in d:
            return False
    except KeyError:
        return True

def handle_users(u):
    users = u
    signal(SIGTERM, quit)
    signal(SIGINT, quit)

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
            pickled_socket = reduce_handle(clntSock.fileno())
            users[username] = pickled_socket

            print "{"
            for keys, values in users.items():
                print keys + ":", values
            print "}"
        elif (action == "EXIT"):
            fd = rebuild_handle(users[username])
            quitSock = fromfd(fd, AF_INET, SOCK_STREAM)
            quitSock.close()
            del users[username]
            clntSock.close()

            print "{"
            for keys, values in users.items():
                print keys + ": ", values
            print "}"

        clntFile.close()
