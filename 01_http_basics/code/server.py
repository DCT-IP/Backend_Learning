# using pythonbasics.org, docs.python.org
# we are going to do 
# socket()
# ↓
# bind()
# ↓
# listen()
# ↓
# accept()
# ↓
# recv()
# ↓
# parse HTTP yourself
# ↓
# build HTTP response yourself
# ↓
# send()
# ↓
# close()

import socket

HOST = 'localhost'
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1) #only 1 for now
    print("Waiting for connection...\n")
    conn, addr = s.accept()
    with conn:
        print(f'Connected by {addr}')
        while True:
            data = conn.recv(1024)
            request = data.decode("utf-8")
            print(request)
            if not data: break
            conn.sendall(data)


##today's session done
#tom will add 
#  parse request
#  build response
#  routing 
#  mutliple methods
#  status codes