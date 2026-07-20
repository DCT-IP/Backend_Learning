INSERT INTO Users (FirstName, LastName, EMAIL) VALUES
('Alice', 'Smith', 'alice.smith@email.com'),
('Bob', 'Johnson', 'bob.j@email.com'),
('Charlie', 'Brown', 'charlie.b@email.com'),
('David', 'Wilson', 'david.w@email.com'),
('Emma', 'Thomas', 'emma.t@email.com');

INSERT INTO Books (BookName, Author, Publisher, Price, Quantity) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', 'Scribner', 14.99, 5),
('To Kill a Mockingbird', 'Harper Lee', 'J.B. Lippincott & Co.', 12.50, 3),
('1984', 'George Orwell', 'Secker & Warburg', 10.99, 4),
('Clean Code', 'Robert C. Martin', 'Prentice Hall', 44.99, 6),
('Design Patterns', 'GoF', 'Addison-Wesley', 54.99, 2),
('The Pragmatic Programmer', 'Andrew Hunt', 'Addison-Wesley', 49.99, 5),
('Introduction to Algorithms', 'CLRS', 'MIT Press', 89.99, 4);

INSERT INTO BorrowRecords
(U_ID, B_ID, borrow_date, return_date, status)
VALUES
(1,1,'2026-07-01','2026-07-15','Returned'),
(2,1,'2026-07-16',NULL,'Borrowed'),
(3,3,'2026-06-01',NULL,'Overdue'),
(1,4,'2026-05-10','2026-05-25','Returned'),
(4,2,'2026-07-05','2026-07-20','Returned'),
(5,6,'2026-07-18',NULL,'Borrowed'),
(2,5,'2026-04-10','2026-04-22','Returned'),
(3,7,'2026-07-02',NULL,'Borrowed'),
(4,4,'2026-03-15','2026-03-28','Returned'),
(5,2,'2026-06-10',NULL,'Overdue');        

IINSERT INTO Reviews
(U_ID, B_ID, rating, comment)
VALUES
(1,1,4.5,'A timeless classic.'),
(2,3,5.0,'Still incredibly relevant.'),
(3,2,3.0,'Good, but school made it less enjoyable.'),
(4,4,5.0,'Must-read for every software engineer.'),
(5,6,4.8,'Excellent programming advice.'),
(2,5,4.2,'Classic software engineering book.'),
(3,7,5.0,'A difficult but fantastic textbook.'),
(1,2,4.0,'Loved the characters.');