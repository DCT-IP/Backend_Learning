# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 8080              # The same port as used by the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'GET / HTTP/1.1\r\nHost: localhost\r\n\r\n')
    data = s.recv(1024)
print('Received', repr(data))