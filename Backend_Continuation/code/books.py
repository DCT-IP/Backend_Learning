from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    HTTPException,
    status,
)
from sqlalchemy.orm import Session
from typing import List

import crud
import schemas
from cache_service import cache
from db import get_db
from dependencies import get_current_user
from tasks import log_book_created

router = APIRouter(prefix="/books", tags=["Books"])


@router.post(
    "/",
    response_model=schemas.BookResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_book(
    book: schemas.BookCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    db_book = crud.create_book(db=db, book=book)
    cache.clear()
    background_tasks.add_task(
        log_book_created,
        db_book.B_ID,
        db_book.BookName,
    )
    return db_book


@router.get("/", response_model=List[schemas.BookResponse])
def read_books(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    cache_key = f"books:list:{skip}:{limit}"
    cached_books = cache.get(cache_key)
    if cached_books is not None:
        return cached_books
    books = crud.get_books(db=db, skip=skip, limit=limit)
    books_data = [
        {
            "B_ID": book.B_ID,
            "BookName": book.BookName,
            "Author": book.Author,
            "Publisher": book.Publisher,
            "Price": book.Price,
            "Quantity": book.Quantity,
        }
        for book in books
    ]
    cache.set(cache_key, books_data, ttl=60)
    return books_data


@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    return db_book


@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(
    book_id: int,
    book: schemas.BookUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    db_book = crud.update_book(
        db=db,
        book_id=book_id,
        book_update=book,
    )
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    cache.clear()
    return db_book


@router.delete(
    "/{book_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_book(
    book_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Book not found",
        )
    cache.clear()
    return None
