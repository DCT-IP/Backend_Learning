# Echo client program
import socket

HOST = 'localhost'
PORT = 8080

def send_test_request(request_string, description):
    print(f"\n=== Testing: {description} ===")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(request_string.encode('utf-8'))
        response = s.recv(4096)
        print(response.decode('utf-8'))

send_test_request("GET / HTTP/1.1\r\nHost: localhost\r\n\r\n", "GET Home Page")
send_test_request("GET /about HTTP/1.1\r\nHost: localhost\r\n\r\n", "GET About Page")
post_req = "POST /submit HTTP/1.1\r\nHost: localhost\r\nContent-Length: 13\r\n\r\nusername=alice"
send_test_request(post_req, "POST Data Submission")
send_test_request("GET /nowhere HTTP/1.1\r\nHost: localhost\r\n\r\n", "GET Missing Page (404)")