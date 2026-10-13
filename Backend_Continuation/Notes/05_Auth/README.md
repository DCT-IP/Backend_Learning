# Session 05 — Authentication & Authorization with JWT
## Overview
This session extends the Library Management API by adding authentication and authorization.
Until Session 4, anyone could interact with every endpoint. In a real application this is unacceptable. Users must first identify themselves, prove their identity, and then be granted permissions based on who they are.
This session implements a complete authentication pipeline using FastAPI, SQLAlchemy, MySQL, bcrypt password hashing, and JWT (JSON Web Tokens).
---
## Objectives
- Understand Authentication vs Authorization
- Learn password hashing using bcrypt
- Store hashed passwords securely
- Register new users
- Login using credentials
- Generate JWT access tokens
- Protect API routes using OAuth2
- Retrieve the currently logged-in user
- Understand FastAPI dependency injection for security
---
## Technologies
- FastAPI
- SQLAlchemy ORM
- MySQL
- Pydantic
- Passlib (bcrypt)
- python-jose (JWT)
- OAuth2PasswordBearer
- Dependency Injection
---
## Authentication Flow
```
Register User
      │
      ▼
Validate Request
      │
      ▼
Hash Password
      │
      ▼
Store User in Database
──────────────────────────────
Login
      │
      ▼
Verify Password
      │
      ▼
Generate JWT Token
      │
      ▼
Return Token
──────────────────────────────
Protected Endpoint
      │
      ▼
Receive Bearer Token
      │
      ▼
Verify JWT
      │
      ▼
Load Current User
      │
      ▼
Allow Request
```
---
## Concepts Covered
### Password Hashing
- bcrypt
- Hashing vs Encryption
- Why passwords should never be stored directly
---
### Authentication
Verify who the user is.
Example:
```
Username + Password
```
---
### Authorization
Determine what an authenticated user can access.
Example:
```
Admin
can delete books
User
cannot
```
---
### JWT
Understanding:
- Header
- Payload
- Signature
- Expiration
- Secret Key
---
### OAuth2
Using
```
OAuth2PasswordBearer
```
to secure endpoints.
---
### Dependency Injection
FastAPI automatically injects the authenticated user using
```
Depends()
```
---
## Endpoints
### User
- POST /register
- POST /login
- GET /me
### Protected
- GET /books
- POST /books
- PUT /books/{id}
- DELETE /books/{id}
(Protected using JWT.)
---
## Learning Outcomes
After completing this session you should be able to
- Build secure authentication systems
- Hash passwords correctly
- Generate JWT tokens
- Verify JWT tokens
- Protect endpoints
- Understand FastAPI security architecture
- Understand dependency injection for authentication
---
