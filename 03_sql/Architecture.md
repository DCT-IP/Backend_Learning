# Module 03 - SQL Fundamentals
## Goal
Learn how relational databases store, retrieve, and manage structured data.
Instead of storing data in Python lists or dictionaries, we move to a persistent SQL database using MySQL.
---
# Architecture
```
                    Client
                       │
                       ▼
              SQL Query (SELECT/INSERT...)
                       │
                       ▼
               MySQL Query Engine
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      Users          Books       BorrowRecords
                                      │
                                      ▼
                                  Reviews
```
---
# Database Schema

```
Users
------
U_ID (PK)
FirstName
LastName
Email

        │
        │ 1
        │
        │
        ▼
BorrowRecords
-------------
borrow_ID (PK)
U_ID (FK)
B_ID (FK)
borrow_date
return_date
status
        ▲
        │
        │
        │
Books
------
B_ID (PK)
BookName
Author
Publisher
Price
Quantity

        ▲
        │
        │
Reviews
--------
review_ID (PK)
U_ID (FK)
B_ID (FK)
rating
comment
```
---
# Relationships
Users
- One user can borrow many books.
- One user can write many reviews.

Books
- One book can be borrowed many times.
- One book can have many reviews.

BorrowRecords
- Connects Users and Books.
- Stores every borrowing event.

Reviews
- Connects Users and Books.
- Stores user feedback.
---
# Data Flow
```
Application
    │
    ▼
SQL Query
    │
    ▼
MySQL Database
    │
    ▼
Rows Returned
    │
    ▼
Application
```
---
# Concepts Learned
- Database Design
- Primary Keys
- Foreign Keys
- Constraints
- Normalization
- INSERT
- SELECT
- WHERE
- ORDER BY
- LIMIT
- DISTINCT
- INNER JOIN
- LEFT JOIN
---
# Design Decisions
- AUTO_INCREMENT used for all primary keys.
- Foreign keys maintain referential integrity.
- CHECK constraints validate prices, ratings, and borrow status.
- Borrow history is stored as events instead of counters.
- Reviews are stored separately to avoid data duplication.
---
