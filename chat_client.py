#!/usr/bin/python
from sys import argv, stdin
from socket import *
from signal import *

if len(argv) != 2:
    print "Usage: ./server.py [host]"
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

sockFile = sock.makefile("rw", 0)


while True:
    for line in sockFile:
        print line

    for line in stdin:
        sock.send(line)
