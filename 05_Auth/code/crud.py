from sqlalchemy.orm import Session
from sqlalchemy import select
import models, schemas
from security import hash_password

def get_book(db: Session, book_id: int):
    return db.scalar(select(models.Book).where(models.Book.B_ID == book_id))

def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.scalars(select(models.Book).offset(skip).limit(limit)).all()

def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, book_update: schemas.BookUpdate):
    db_book = get_book(db, book_id)
    if not db_book:
        return None
    update_data = book_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_book, key, value)
        
    db.commit()
    db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book

def get_user_by_email(db: Session, email: str):
    return db.scalar(
        select(models.User).where(models.User.Email == email)
    )


def create_user(db: Session, user: schemas.UserCreate):
    password_hash = hash_password(user.Password)

    db_user = models.User(
        FirstName=user.FirstName,
        LastName=user.LastName,
        Email=user.Email,
        PasswordHash=password_hash
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user