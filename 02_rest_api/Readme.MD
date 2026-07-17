# Module 02 — REST API Design

## Objective
The goal of this module is to understand the principles of REST APIs and implement a complete CRUD application using FastAPI.
Instead of focusing on databases or authentication, this module concentrates on designing clean HTTP endpoints, validating incoming data, and returning appropriate HTTP responses.
---
## Learning Outcomes
By the end of this module, I should understand:
- REST Architecture
- Resources and Resource-Oriented Design
- CRUD Operations
- HTTP Methods
- Path Parameters
- Query Parameters
- Request Bodies
- Response Models
- HTTP Status Codes
- Request Validation using Pydantic
- Error Handling using HTTPException
---
## Technologies Used
- Python 3.x
- FastAPI
- Pydantic
- Uvicorn
---
## Project
A simple **Books API** implementing CRUD operations using an in-memory Python list instead of a database.
---
## Project Structure
```
02_rest_api/

README.md
architecture.md
code/
│
├── main.py
├── models.py
└── database.py
```
---
## Features
- Create a Book
- Read all Books
- Read a Book by ID
- Update a Book
- Delete a Book
- Filter Books by Author
- Filter Books by Maximum Price
- Automatic Request Validation
- Proper HTTP Status Codes
- Interactive API Documentation
---
## API Endpoints
| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/` | Welcome Route |
| GET | `/books` | Retrieve all books |
| GET | `/books/{id}` | Retrieve a single book |
| POST | `/books` | Create a new book |
| PUT | `/books/{id}` | Replace an existing book |
| DELETE | `/books/{id}` | Delete a book |
---
## Query Parameters

### Filter by Author
```
GET /books?author=Robert
```
### Filter by Maximum Price
```
GET /books?max_price=50
```
---
## HTTP Status Codes Used
| Status Code | Meaning |
|-------------|---------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 400 | Bad Request |
| 404 | Not Found |
| 422 | Validation Error |
---
## Validation
The Book model validates:
- Positive Price
- Positive Borrow Duration
- Correct Data Types
- Required Fields
Validation is handled automatically using Pydantic.
---
## Running the Project
Install dependencies
```bash
pip install fastapi uvicorn
```
Run the server
```bash
uvicorn main:app --reload
```
Server
```
http://127.0.0.1:8000
```
Interactive API Docs
```
http://127.0.0.1:8000/docs
```
Alternative Documentation
```
http://127.0.0.1:8000/redoc
```
---
## Example Request
```json
{
    "id": 1,
    "name": "Clean Code",
    "author": "Robert C. Martin",
    "publisher": "Prentice Hall",
    "price": 49.99,
    "days_borrowed": 7
}
```
---
## Workflow Followed
```
Understand REST
↓
Design Resources
↓
Design Endpoints
↓
Create Pydantic Models
↓
Implement CRUD
↓
Validate Requests
↓
Handle Errors
↓
Test Using Swagger UI
↓
Refactor
```
---
## Challenges Faced
- Understanding REST resource naming.
- Choosing appropriate HTTP methods.
- Returning correct HTTP status codes.
- Validating request bodies using Pydantic.
- Designing filtering using query parameters.
- Separating models and application logic into different files.
---
## Key Takeaways
- REST focuses on resources rather than actions.
- HTTP methods define the operation performed on a resource.
- Pydantic greatly simplifies validation.
- FastAPI automatically generates API documentation.
- Proper status codes make APIs predictable and easier to consume.
- Even a simple CRUD application benefits from clean project organization.
---
