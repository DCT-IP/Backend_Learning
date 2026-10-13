# Architecture — Session 05
## Overview
Authentication is introduced as a separate layer between the client and the application.
Instead of directly accessing the database, every request requiring authentication first passes through the security pipeline.
---
## Overall Architecture
```
                 Client
                    │
      POST /register
      POST /login
      GET /books
                    │
              FastAPI Router
                 (main.py)
                    │
        ┌───────────┴───────────┐
        │                       │
        ▼                       ▼
    Authentication          CRUD Layer
      (auth.py)             (crud.py)
        │                       │
        ▼                       ▼
 Password Hashing          SQLAlchemy ORM
        │                       │
        └───────────┬───────────┘
                    │
                models.py
                    │
             SQLAlchemy Engine
                    │
                MySQL Database
```
---
# File Responsibilities
## db.py
Responsible for
- Creating Engine
- SessionLocal
- Base
- Database Connection
- Dependency Injection (get_db)
---
## models.py
Represents the database tables.
Contains SQLAlchemy ORM models.
Responsible for
- Table definitions
- Relationships
- Constraints
Represents
```
Database
```
---
## schemas.py
Represents API request and response models.
Responsible for
- Input validation
- Output serialization
- Data transfer
Represents
```
HTTP Layer
```
---
## crud.py
Contains all database operations.
Examples
- Create Book
- Read Book
- Update Book
- Delete Book
CRUD should never know anything about HTTP.
---
## auth.py
Contains authentication logic.
Responsible for
- Password Hashing
- Password Verification
- JWT Creation
- JWT Verification
This file never communicates directly with FastAPI routes.
---
## dependencies.py
Contains reusable authentication dependencies.
Examples
```
get_current_user()
get_current_active_user()
```
Routes simply reuse these functions.
---
## main.py
Responsible only for
- API Routes
- HTTP Status Codes
- Calling CRUD
- Calling Authentication
- Returning Responses
Business logic should remain outside this file.
---
# Authentication Flow
```
Client
   │
POST /register
   │
schemas.py
   │
auth.py
(Hash Password)
   │
crud.py
(Store User)
   │
models.py
   │
MySQL
```
---
# Login Flow
```
Client
   │
POST /login
   │
schemas.py
   │
crud.py
(Get User)
   │
auth.py
Verify Password
Generate JWT
   │
Return Token
```
---
# Protected Route Flow
```
Client
Bearer Token
      │
Depends(get_current_user)
      │
auth.py
Verify JWT
      │
crud.py
Retrieve User
      │
Route Executes
```
---
# Layer Responsibilities
```
models.py
        ↓
Represents data at rest
(Database Tables / SQLAlchemy ORM)
schemas.py
        ↓
Represents data in motion
(HTTP Request/Response Validation)

crud.py
        ↓
Encapsulates data access patterns
(SQLAlchemy Queries & Transactions)

auth.py
        ↓
Encapsulates security
(Hashing, JWT, Verification)

dependencies.py
        ↓
Provides reusable authentication dependencies

main.py
        ↓
Handles routing, HTTP protocol details,
dependency injection, and status codes.
```
---
# Design Principle
Each layer has one responsibility.
```
main.py
↓
auth.py
↓
crud.py
↓
models.py
↓
MySQL
```