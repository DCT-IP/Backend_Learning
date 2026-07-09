# Notes for Socket Programming
Via: https://docs.python.org/3/library/socket.html

 - python interface is transliteration of UNIX system call and library interface for sockets to python's OOP style
 - *socket()* returns a socket object, whose methods implement the various socket system cals

## Core Concepts
 - the syntax is 
 ``` python
 socket.socket(family, type)
 ```
 - AF_INET -> address family for IPV4
 - AF_INET6 -> address family for IPV6
 - SOCK_STREAM: socket for TCP, provides relable, sequenced connection-oriented communication
 - SOCK_DGRAM: socket for UDP
---
## Our working 
 - we will first create a server, that will initialize a socket, that will bind and listen, accept connection, recive data and close the connection
 - a client will be made too that will send a message and wait for response
---
## How to bind, listen and accept and recieve and send
### bind()
Associates a socket with a local IP address and port.

Without binding, the OS does not know on which port the server should listen for incoming connections.

### listen()
Marks the socket as a passive socket.

Instead of initiating connections, it waits for incoming connection requests.

The backlog parameter specifies the maximum number of queued connections.

### accept()
Blocks until a client connects.

Returns

- a new socket object connected to the client
- the client's address

The listening socket continues waiting for new connections.

Each client gets its own socket.

### recv()
Receives bytes from the connected client.

Returns bytes, not strings.

Usually decoded using UTF-8.

### send()
Sends bytes to the client.

HTTP responses must therefore be encoded before being sent.
---