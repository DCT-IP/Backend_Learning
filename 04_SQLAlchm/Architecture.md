# Module 04 Architecture
## High-Level Architecture
```text
                HTTP Request
                      │
                      ▼
                ┌────────────┐
                │  main.py   │
                └────────────┘
                      │
          Depends(get_db) / Routing
                      │
                      ▼
                ┌────────────┐
                │  crud.py   │
                └────────────┘
                      │
            ORM Queries & Transactions
                      │
                      ▼
                ┌────────────┐
                │ models.py  │
                └────────────┘
                      │
          SQLAlchemy ORM Mapping
                      │
                      ▼
                ┌────────────┐
                │   MySQL    │
                └────────────┘
```
---
# Layer Responsibilities
## db.py
Responsible for infrastructure.
Creates
- Engine
- SessionLocal
- Base
Acts as the bridge between Python and MySQL.
---
## models.py
Represents **data at rest (Database Tables / SQLAlchemy ORM).**
Responsibilities
- Table Definitions
- Columns
- Constraints
- Relationships
- Foreign Keys
Maps Python classes to SQL tables.
---
## schemas.py
Represents **data in motion (HTTP Request/Response validation / Pydantic).**
Responsibilities
- Validate incoming data
- Serialize outgoing data
- Define request bodies
- Define response models
Schemas never communicate directly with the database.
---
## crud.py
Encapsulates **data access patterns (ORM Queries & Transactions).**
Responsibilities
- Query database
- Insert records
- Update records
- Delete records
- Commit transactions
- Rollback on failure
This is the only layer that should interact with SQLAlchemy Sessions.
---
## main.py
Handles **routing, HTTP protocol details, & status codes.**
Responsibilities
- API Routes
- HTTP Methods
- Status Codes
- Dependency Injection
- Calling CRUD functions
- Returning API Responses
Business logic should not live here.
---
# Request Flow
```text
Client

↓

main.py

↓

schemas.py
(Request Validation)

↓

crud.py

↓

models.py

↓

SQLAlchemy Session

↓

MySQL
```
---
# Response Flow
```text
MySQL

↓

SQLAlchemy ORM Objects

↓

crud.py

↓

main.py

↓

schemas.py
(Response Serialization)

↓

JSON Response

↓

Client
```
---

# Separation of Concerns

```text
database.py
│
├── Database Configuration
├── Engine
└── Sessions

models.py
│
├── Database Structure
├── ORM Models
└── Relationships

schemas.py
│
├── API Contracts
├── Validation
└── Serialization

crud.py
│
├── Database Operations
├── Transactions
└── ORM Queries

main.py
│
├── API Endpoints
├── Routing
└── HTTP Responses
```

# End-to-End Flow

```text
Browser / Postman

↓

FastAPI Endpoint

↓

Pydantic Schema

↓

CRUD Function

↓

SQLAlchemy Session

↓

ORM Model

↓

MySQL Database

↓

ORM Model

↓

Pydantic Schema

↓

JSON Response
```