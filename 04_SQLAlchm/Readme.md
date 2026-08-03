# Module 04 — SQLAlchemy ORM
## Overview
In this module, we replace raw SQL interactions with SQLAlchemy ORM while keeping the same MySQL database designed in Module 03. Instead of manually writing SQL queries for every operation, SQLAlchemy maps Python classes to database tables and translates ORM operations into SQL.

This module also introduces a clean backend architecture by separating database models, request/response schemas, CRUD logic, and API routes.
---
## Objectives
- Connect FastAPI to a MySQL database.
- Configure SQLAlchemy Engine and Sessions.
- Model existing database tables using ORM.
- Understand the difference between ORM Models and Pydantic Schemas.
- Perform CRUD operations using SQLAlchemy Sessions.
- Integrate SQLAlchemy with FastAPI Dependency Injection.
- Replace the in-memory database from Module 02 with MySQL.
---
## Folder Structure
```text
04_sqlalchemy/

README.md
architecture.md

code/
│
├── database.py
├── models.py
├── schemas.py
├── crud.py
├── main.py
└── .env
```
---
## Responsibilities
### db.py
Responsible for
- Loading environment variables
- Creating the SQLAlchemy Engine
- Creating SessionLocal
- Defining the Declarative Base
---
### models.py
Represents data at rest (Database Tables / SQLAlchemy ORM).
Contains
- SQLAlchemy Models
- Table Definitions
- Relationships
- Constraints
- Foreign Keys
---
### schemas.py
Represents data in motion (HTTP Request/Response validation / Pydantic).
Contains
- Request Schemas
- Response Schemas
- Validation Rules
- Serialization
---
### crud.py
Encapsulates data access patterns (ORM Queries & Transactions).
Contains
- Create
- Read
- Update
- Delete
- Transaction Management
---
### main.py
Handles routing, HTTP protocol details, & status codes.
Contains
- API Endpoints
- Dependency Injection
- HTTP Status Codes
- Response Models
---
## Workflow
```text
HTTP Request

↓

FastAPI Route

↓

Pydantic Validation

↓

CRUD Layer

↓

SQLAlchemy Session

↓

ORM Models

↓

MySQL Database

↓

ORM Objects

↓

Pydantic Response

↓

JSON Response
```
---
## Learning Outcomes
After completing this module, I should be able to
- Configure SQLAlchemy from scratch.
- Connect FastAPI to MySQL.
- Design ORM Models.
- Understand ORM Relationships.
- Separate Models, Schemas, CRUD, and Routes.
- Implement CRUD operations using SQLAlchemy.
- Replace raw SQL with ORM where appropriate.
- Build scalable backend architecture.
---
## References
- SQLAlchemy ORM Quick Start
- SQLAlchemy ORM Query Guide
- FastAPI SQL Databases
- SQLAlchemy Core Documentation