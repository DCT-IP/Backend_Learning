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
# we adding :
#  parse request
#  build response
#  routing 
#  mutliple methods
#  status codes

import socket

HOST = 'localhost'
PORT = 8080
class Request:
    def __init__(self, method, path, version, headers, body):
        self.method = method
        self.path = path
        self.version = version
        self.headers = headers
        self.body = body

def home(request):
    return (
        200,
        "OK",
        "<h1>Welcome!</h1>"
    )


def about(request):
    return (
        200,
        "OK",
        "<h1>About</h1><p>This was made entirely using Python sockets.</p>"
    )


def submit(request):
    return (
        200,
        "OK",
        f"<h1>Received:</h1><p>{request.body}</p>"
    )

def parse_request(request_text):
    if not request_text.strip():
        return None
    parts = request_text.split("\r\n\r\n", 1)
    header_part = parts[0]
    body = parts[1] if len(parts) > 1 else ""
    lines = header_part.split("\r\n")
    method, path, version = lines[0].split()
    headers = {}
    for line in lines[1:]:
        key, value = line.split(":", 1)
        headers[key.strip()] = value.strip()
    return Request(method, path, version, headers, body)
routes = {
    ("GET", "/"): home,
    ("GET", "/about"): about,
    ("POST", "/submit"): submit,
}
def route_request(request):
    handler = routes.get((request.method, request.path))

    if handler:
        return handler(request)

    return (
        404,
        "Not Found",
        "<h1>404 Not Found</h1>"
    )
def build_response(status_code, status_text, body_content, content_type="text/html"):
    """Constructs a valid plain-text HTTP response string."""
    body_bytes = body_content.encode('utf-8')
    
    response_headers = [
        f"HTTP/1.1 {status_code} {status_text}",
        f"Content-Type: {content_type}; charset=utf-8",
        f"Content-Length: {len(body_bytes)}",
        "Connection: close", 
    ]
    header_string = "\r\n".join(response_headers) + "\r\n\r\n"
    return header_string.encode('utf-8') + body_bytes
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(5) 
    print(f"Server serving HTTP on port {PORT}...")

    while True:
        conn, addr = s.accept()
        with conn:
            data = conn.recv(2048)
            if not data: 
                continue
                
            request_text = data.decode("utf-8")
            print(f"--- RECEIVED REQUEST FROM {addr} ---\n{request_text}")

            try:
                request = parse_request(request_text)

                status_code, status_text, body_content = route_request(request)

                response_bytes = build_response(
                                                    status_code,
                                                    status_text,
                                                    body_content
                                                )

                conn.sendall(response_bytes)

            except Exception as e:
                status_code, status_text = "500", "Internal Server Error"
                body_content = f"<h1>500 Server Error</h1><p>{str(e)}</p>"

            response_bytes = build_response(status_code, status_text, body_content)
            conn.sendall(response_bytes)
