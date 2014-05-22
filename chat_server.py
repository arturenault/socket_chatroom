#!/usr/bin/python

from user_handler import *
from multiprocessing import Process, Manager
from signal import *

manager = Manager()
users = manager.dict()

user_h = Process(target=handle_users, args=(users,))
user_h.start()

def quit(signum, frame):
    user_h.terminate()
    print "Chat server terminated."
    exit(0)

signal(SIGINT, quit)

while True:
    messages = ""
    if not dict_is_empty(users):
        for each in users:
            fd = rebuild_handle(users[each])
            sock = fromfd(fd, AF_INET, SOCK_STREAM)
            sockFile = users[each].open()
        for line in sockFile:
            message = username + ": " + line
    if messages != "":
        for each in users:
            users[each].send(messages)
