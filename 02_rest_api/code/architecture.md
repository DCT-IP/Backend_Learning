# Books API Architecture
## Overview
This project is a simple REST API built using FastAPI. The objective is to understand how HTTP requests are handled, validated, processed, and returned to the client before introducing databases and more advanced backend concepts.
---
## High-Level Architecture
```
                Client
                   │
                   │ HTTP Request
                   ▼
             FastAPI Router
                   │
                   ▼
          Endpoint Function
                   │
                   ▼
          In-Memory Database
            (Python List)
                   │
                   ▼
         Pydantic Validation
                   │
                   ▼
             HTTP Response
                   │
                   ▼
                Client
```
---
## Project Structure
```
02_rest_api/
code/
│
├── main.py
├── models.py
└── database.py

README.md
exercise.md
architecture.md
```
---
## Components
### `main.py`
Responsible for:
- Receiving HTTP requests
- Routing requests to the correct endpoint
- Returning HTTP responses
- Raising appropriate HTTP exceptions
---
### `models.py`
Contains all Pydantic models.
Responsibilities:
- Define the structure of a Book
- Validate incoming request data
- Ensure correct data types
Example:
```python
class Book(BaseModel):
    id: int
    name: str
    author: str
    publisher: str
    price: float
    days_borrowed: int
```
---
### `database.py`
Contains the temporary in-memory database.
```python
DB = []
```
Responsibilities:
- Store all books while the application is running
- Simulate a real database
---
## Request Flow
Example: Creating a Book
```
Client
    │
    │ POST /books
    ▼
FastAPI Router
    │
    ▼
create_book()
    │
    ▼
Pydantic validates request
    │
    ▼
Book appended to DB
    │
    ▼
201 Created Response
    │
    ▼
Client
```
---
## CRUD Flow
### Create
```
POST /books
        │
        ▼
Validate Book
        │
        ▼
Append to DB
        │
        ▼
Return 201 Created
```
---
### Read
```
GET /books
        │
        ▼
Read DB
        │
        ▼
Return list of books
```
---
### Update
```
PUT /books/{id}
        │
        ▼
Find book
        │
        ▼
Replace existing book
        │
        ▼
Return updated book
```
---
### Delete

```
DELETE /books/{id}
        │
        ▼
Find book
        │
        ▼
Remove from DB
        │
        ▼
Return 204 No Content
```
---
## Why Pydantic?
Pydantic automatically validates incoming request data before our endpoint executes.
It checks:
- Required fields
- Correct data types
- Custom validation rules
- Invalid inputs
If validation fails, FastAPI automatically returns a `422 Unprocessable Entity` response.
---
## Why Use an In-Memory Database?
Instead of learning SQL immediately, a Python list allows us to focus on:
- REST API design
- HTTP methods
- Routing
- Validation
- Status codes
In later modules, this list will be replaced with a real PostgreSQL database.
---
## Current Limitations
Since this project uses an in-memory list:
- Data is lost when the server stops.
- No persistent storage.
- No authentication.
- No pagination.
- No sorting.
- Searching is linear (`O(n)`).

These limitations will be addressed in future modules.
---
## Request Lifecycle

```
HTTP Request
      │
      ▼
FastAPI Router
      │
      ▼
Endpoint Function
      │
      ▼
Business Logic
      │
      ▼
In-Memory Database
      │
      ▼
Pydantic Response Model
      │
      ▼
HTTP Response
```
---
