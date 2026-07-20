/*
Database: library_db

Purpose:
This database models a simple Library Management System.

Entities:
1. Users - stores library members.
2. Books - stores available books.
3. BorrowRecords - records every borrowing transaction.
4. Reviews - stores user reviews for books.

Relationships:
Users (1) ---- (N) BorrowRecords
Books (1) ---- (N) BorrowRecords

Users (1) ---- (N) Reviews
Books (1) ---- (N) Reviews

Design Decisions:
- AUTO_INCREMENT is used for all primary keys.
- Email is UNIQUE.
- Price uses DECIMAL(10,2) for monetary accuracy.
- Borrow history is stored as events rather than counters.
- Reviews are stored separately to avoid redundancy.
*/
CREATE DATABASE library_manage;
use library_manage;

CREATE TABLE Users(
    U_ID int AUTO_INCREMENT PRIMARY KEY,
    FirstName varchar(255) NOT NULL,
    LastName varchar(255) NOT NULL ,
    EMAIL varchar(255) NOT NULL UNIQUE
);

CREATE TABLE Books(
    B_ID int AUTO_INCREMENT PRIMARY KEY,
    BookName VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Publisher VARCHAR(255) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    Quantity INT NOT NULL,
    CCONSTRAINT chk_price CHECK (Price >= 0.0),
    CONSTRAINT chk_quantity CHECK (Quantity >= 0)
);

CREATE TABLE BorrowRecords(
    borrow_ID int AUTO_INCREMENT PRIMARY KEY,
    U_ID int NOT NULL,
    B_ID int NOT NULL,
    borrow_date date NOT NULL,
    return_date date,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (U_ID) REFERENCES Users(U_ID),
    FOREIGN KEY (B_ID) REFERENCES Books(B_ID),
    CONSTRAINT chk_status CHECK (status IN ('Borrowed', 'Returned', 'Overdue'))
);

CREATE TABLE Reviews(
    review_id int AUTO_INCREMENT PRIMARY KEY,
    U_ID int NOT NULL,
    B_ID int NOT NULL,
    rating float,
    comment TEXT,
    FOREIGN KEY (U_ID) REFERENCES Users(U_ID),
    FOREIGN KEY (B_ID) REFERENCES Books(B_ID),
    CONSTRAINT chk_review_rating CHECK (rating BETWEEN 0.0 AND 5.0)
);