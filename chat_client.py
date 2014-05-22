#!/usr/bin/python
from sys import argv, stdin
from signal import *
from select import *
from socket import *

if len(argv) != 2:
    print "Usage: %s [host]" % argv[0]
    exit(1)

host = gethostbyname(argv[1])
port = 19940

print "Welcome to multichat!"
username = raw_input("username: ")

sock = socket(AF_INET, SOCK_STREAM)

def quit(signum, frame):
    sock.close()
    quitSock = socket(AF_INET, SOCK_STREAM)
    quitSock.connect((host, port))
    quitSock.send("EXIT " + username + "\n")
    quitSock.close()
    print "You have left the chat."
    exit(0)

signal(SIGINT, quit)

try:
    sock.connect((host, port))
except error:
    print "Connection failed."
    exit(1)

sock.send("ENTER " + username + "\n")

sock.setblocking(0)

while True:
    while stdin in select([stdin], [], [], 0)[0]:
        line = stdin.readline()
        if line:
            sock.send(username + ": " + line)
    else:
        try:
            messages = sock.recv(4096)
            print messages
        except error:
            pass
