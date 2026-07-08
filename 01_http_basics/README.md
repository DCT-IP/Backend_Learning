# Session 1 — HTTP Fundamentals & Socket Programming

## Objective

Understand how the web actually works by building a minimal HTTP server from scratch before relying on frameworks.

The goal is to understand what FastAPI, Flask, Express, or Spring are doing underneath.

---

## Learning Outcomes

By the end of this session, I should be able to explain

- What happens after entering a URL in a browser
- Client-Server Architecture
- TCP vs HTTP
- Sockets
- HTTP Requests
- HTTP Responses
- HTTP Methods
- HTTP Headers
- Status Codes
- JSON as a data exchange format
- Stateless communication

---

## Documentation

Primary Sources

- MDN HTTP Documentation
- MDN HTTP Messages
- MDN HTTP Methods
- MDN HTTP Status Codes
- Python Socket Documentation
- FastAPI Introduction (only after understanding HTTP)

---

## Topics

### Networking Basics

- IP Address
- Port
- DNS
- TCP
- Client
- Server
- Socket

---

### HTTP

- Request Line
- Response Line
- Headers
- Body
- Methods
- Status Codes
- Cookies
- Content Types

---

### Socket Programming

- Creating sockets
- Binding
- Listening
- Accepting connections
- Receiving data
- Sending responses
- Closing connections

---

## Implementation

Build a tiny HTTP server using Python sockets.

The server should support

- GET
- POST
- PUT
- DELETE

No FastAPI.

No Flask.

No frameworks.

Only Python's standard library.

---

## Suggested Folder Structure

```
01_http_basics/

README.md
exercise.md

code/

    server.py
    router.py
    request.py
    response.py
```

---

## Exercises

- Return plain text
- Return JSON
- Read URL path
- Read query parameters
- Read request body
- Return custom status codes
- Handle unsupported routes
- Handle unsupported methods

---

## Exit Criteria

The session is complete when

- HTTP requests can be parsed manually
- Responses are generated manually
- GET, POST, PUT and DELETE work
- Multiple routes are supported
- Errors return correct status codes
- The entire server can be explained without referring to documentation

---

## Reflection

At the end of this session, document

- What HTTP actually is
- What a socket is
- How TCP differs from HTTP
- How an HTTP request is structured
- How an HTTP response is structured
- What was difficult
- What was learned