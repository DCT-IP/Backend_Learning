/*
Database: library_manage

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

-- CREATE DATABASE library_manage;
USE library_manage;

-- Drop child tables first, then parent tables
DROP TABLE IF EXISTS Reviews;
DROP TABLE IF EXISTS BorrowRecords;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Users;

CREATE TABLE Users(
    U_ID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) NOT NULL UNIQUE
);

CREATE TABLE Books(
    B_ID INT AUTO_INCREMENT PRIMARY KEY,
    BookName VARCHAR(255) NOT NULL,
    Author VARCHAR(255) NOT NULL,
    Publisher VARCHAR(255) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    Quantity INT NOT NULL,
    CONSTRAINT chk_price CHECK (Price >= 0.0),
    CONSTRAINT chk_quantity CHECK (Quantity >= 0)
);

CREATE TABLE BorrowRecords(
    Borrow_ID INT AUTO_INCREMENT PRIMARY KEY,
    U_ID INT NOT NULL,
    B_ID INT NOT NULL,
    Borrow_Date DATE NOT NULL,
    Return_Date DATE,
    Status VARCHAR(20) NOT NULL,
    FOREIGN KEY (U_ID) REFERENCES Users(U_ID),
    FOREIGN KEY (B_ID) REFERENCES Books(B_ID),
    CONSTRAINT chk_status
        CHECK (Status IN ('Borrowed', 'Returned', 'Overdue'))
);

CREATE TABLE Reviews(
    Review_ID INT AUTO_INCREMENT PRIMARY KEY,
    U_ID INT NOT NULL,
    B_ID INT NOT NULL,
    Rating FLOAT NOT NULL,
    Comment TEXT,
    FOREIGN KEY (U_ID) REFERENCES Users(U_ID),
    FOREIGN KEY (B_ID) REFERENCES Books(B_ID),
    CONSTRAINT chk_review_rating
        CHECK (Rating BETWEEN 0.0 AND 5.0)
);