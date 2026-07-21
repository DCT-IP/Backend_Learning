/*
Library Management System Queries
File: queries.sql
Database: library_manage
*/

USE library_manage;

-- ===================================================================
-- Basic Select & Filtering Queries (q1 - q4)
-- ===================================================================

-- q1: return every book[cite: 1]
SELECT * 
FROM Books;

-- q2: returning only bookname and author[cite: 1]
SELECT BookName, Author 
FROM Books;

-- q3: Books cost less than 20/-[cite: 1]
SELECT * 
FROM Books
WHERE Price < 20;

-- q4: Books with status as borrowed[cite: 1]
SELECT * 
FROM BorrowRecords
WHERE status = 'Borrowed';

-- ===================================================================
-- ORDER BY & LIMIT Queries
-- ===================================================================

-- q5: Top 3 most expensive books
SELECT BookName, Author, Price 
FROM Books
ORDER BY Price DESC 
LIMIT 3;

-- q6: All books sorted alphabetically by name
SELECT BookName, Author, Price 
FROM Books
ORDER BY BookName ASC;

-- ===================================================================
-- DISTINCT Queries
-- ===================================================================

-- q7: Unique publishers in the library
SELECT DISTINCT Publisher 
FROM Books;

-- q8: Unique borrow statuses available
SELECT DISTINCT status 
FROM BorrowRecords;

-- ===================================================================
-- JOIN Queries
-- ===================================================================

-- q9: Borrow records with user names and book titles (INNER JOIN)
SELECT 
    br.borrow_ID,
    CONCAT(u.FirstName, ' ', u.LastName) AS UserName,
    b.BookName,
    br.borrow_date,
    br.status
FROM BorrowRecords br
JOIN Users u ON br.U_ID = u.U_ID
JOIN Books b ON br.B_ID = b.B_ID;

-- q10: Reviews with reviewer names and book titles sorted by highest rating (INNER JOIN)
SELECT 
    CONCAT(u.FirstName, ' ', u.LastName) AS Reviewer,
    b.BookName,
    r.rating,
    r.comment
FROM Reviews r
JOIN Users u ON r.U_ID = u.U_ID
JOIN Books b ON r.B_ID = b.B_ID
ORDER BY r.rating DESC;

-- q11: All users and their borrow history, including users who haven't borrowed (LEFT JOIN)
SELECT 
    CONCAT(u.FirstName, ' ', u.LastName) AS UserName,
    b.BookName,
    br.status
FROM Users u
LEFT JOIN BorrowRecords br ON u.U_ID = br.U_ID
LEFT JOIN Books b ON br.B_ID = b.B_ID;