from db import Base
from sqlalchemy import Column, Integer, String, Numeric, Date, Text, ForeignKey, CheckConstraint, Float
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'Users'
    U_ID = Column(Integer, primary_key=True, autoincrement=True)
    FirstName = Column(String(255), nullable=False)
    LastName = Column(String(255), nullable=False)
    Email = Column(String(255), nullable=False, unique=True)
    PasswordHash = Column(String(255), nullable=False)
    
    borrow_records = relationship("BorrowRecord", back_populates="user")
    reviews = relationship("Review", back_populates="user")


class Book(Base):
    __tablename__ = "Books"

    B_ID = Column(Integer, primary_key=True, autoincrement=True)
    BookName = Column(String(255), nullable=False)
    Author = Column(String(255), nullable=False)
    Publisher = Column(String(255), nullable=False)
    Price = Column(Numeric(10, 2), nullable=False)
    Quantity = Column(Integer, nullable=False)

    __table_args__ = (
        CheckConstraint("Price >= 0.0", name="chk_price"),
        CheckConstraint("Quantity >= 0", name="chk_quantity"),
    )

    borrow_records = relationship("BorrowRecord", back_populates="book")
    reviews = relationship("Review", back_populates="book")


class BorrowRecord(Base):
    __tablename__ = "BorrowRecords"

    Borrow_ID = Column(Integer, primary_key=True, autoincrement=True)
    U_ID = Column(Integer, ForeignKey("Users.U_ID"), nullable=False)
    B_ID = Column(Integer, ForeignKey("Books.B_ID"), nullable=False)
    Borrow_Date = Column(Date, nullable=False)
    Return_Date = Column(Date, nullable=True)
    Status = Column(String(20), nullable=False)

    __table_args__ = (
        CheckConstraint(
            "Status IN ('Borrowed', 'Returned', 'Overdue')", name="chk_status"
        ),
    )

    user = relationship("User", back_populates="borrow_records")
    book = relationship("Book", back_populates="borrow_records")


class Review(Base):
    __tablename__ = "Reviews"

    Review_ID = Column(Integer, primary_key=True, autoincrement=True)
    U_ID = Column(Integer, ForeignKey("Users.U_ID"), nullable=False)
    B_ID = Column(Integer, ForeignKey("Books.B_ID"), nullable=False)
    Rating = Column(Float, nullable=False)
    Comment = Column(Text, nullable=True)

    __table_args__ = (
        CheckConstraint("Rating BETWEEN 0.0 AND 5.0", name="chk_review_rating"),
    )

    # Relationships (Many-to-One)
    user = relationship("User", back_populates="reviews")
    book = relationship("Book", back_populates="reviews")