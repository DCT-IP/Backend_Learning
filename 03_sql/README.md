# Module 03 — SQL Fundamentals

## Objective
The goal of this module is to learn relational databases and SQL from a backend engineer's perspective.
Instead of memorizing SQL syntax, the focus is on understanding how data is modeled, stored, queried, and maintained efficiently.
By the end of this module, I should be comfortable designing relational schemas and writing SQL queries for real backend applications.
---
## Learning Outcomes
By the end of this module, I should understand:

- Why Databases Exist
- Relational Databases
- Tables
- Rows and Columns
- Primary Keys
- Foreign Keys
- Constraints
- Data Types
- Normalization
- SQL Queries
- Joins
- Aggregate Functions
- Grouping
- Ordering
- Indexes
- Transactions
- ACID Properties
---
## Technologies Used
- PostgreSQL
- pgAdmin / psql
- SQL
---
## Project
Design and implement a small relational database for a **Library Management System**.
The database will contain relationships between:
- Users
- Books
- Borrow Records
- Reviews
The focus is on designing the schema first and then querying it.
---
## Project Structure
```
03_sql/

README.md
architecture.md
code/
│
├── schema.sql
├── queries.sql
└── sample_data.sql
```
---
### Transactions
- BEGIN
- COMMIT
- ROLLBACK
---

## Database Schema
The database consists of four tables.

```
Users
│
├── user_id (PK)
├── name
├── email

Books
│
├── book_id (PK)
├── title
├── author
├── publisher
├── price

BorrowRecords
│
├── borrow_id (PK)
├── user_id (FK)
├── book_id (FK)
├── borrow_date
├── return_date

Reviews
│
├── review_id (PK)
├── user_id (FK)
├── book_id (FK)
├── rating
├── comment
```
---
## Skills Practiced
- Designing relational schemas
- Choosing primary keys
- Creating foreign key relationships
- Writing CRUD queries
- Joining multiple tables
- Aggregating data
- Using transactions
- Optimizing queries with indexes
---
## Example Queries

Retrieve all books.
```sql
SELECT * FROM Books;
```
Find books written by a specific author.
```sql
SELECT *
FROM Books
WHERE author = 'Robert C. Martin';
```
Find every book borrowed by a user.
```sql
SELECT Users.name,
       Books.title
FROM BorrowRecords
INNER JOIN Users
ON BorrowRecords.user_id = Users.user_id
INNER JOIN Books
ON BorrowRecords.book_id = Books.book_id;
```
---
## Workflow Followed
```
Understand Relational Databases
↓
Design Entities
↓
Identify Relationships
↓
Create Tables
↓
Insert Sample Data
↓
Write Queries
↓
Test Queries
↓
Normalize Schema
↓
Optimize Using Indexes
```
---
## Challenges
- Identifying entities and relationships.
- Choosing primary and foreign keys.
- Understanding JOIN operations.
- Avoiding duplicate data through normalization.
- Writing efficient SQL queries.
---
## Key Takeaways
- SQL is a language for interacting with relational databases.
- A well-designed schema is more important than clever queries.
- Relationships are the foundation of relational databases.
- Joins allow data to be reconstructed across multiple tables.
- Constraints maintain data integrity.
- Indexes improve read performance at the cost of additional storage and slower writes.
- Transactions ensure data consistency even when failures occur.
---