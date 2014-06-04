# Socket Chatroom

This is a simple chat room written in Python using very basic sockets.

It works using two main scripts: chat\_server.py and chat\_client.py

chat\_server.py starts a different process called user\_handler.py which manages the entries and exits of the chat room users. It creates sockets for these users, bottles them up and adds them to a dictionary of usernames to bottled sockets which is accessible to chat\_server.py.

chat\_client.py takes in the host of the server (which should already be running), asks for a username, and joins the list of users by sending a message to user\_handler.py in the form "ENTER <username>"

chat\_server.py then iterates through all the sockets in the dictionary and compiles all the received messages, and then sends them out to all the sockets by iterating through them again. I suspect this is not the most efficient way to do this.

Anyhow, it isn't working yet. It can manage users, but not relay messages. I appreciate any help on this one, I'm just doing it for practice (:
