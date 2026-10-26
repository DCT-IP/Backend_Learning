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
    background_tasks.add_task(
        log_book_created,
        db_book.B_ID,
        db_book.BookName,
    )
    return db_book

@router.get("/", response_model=List[schemas.BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return crud.get_books(db=db, skip=skip, limit=limit)

@router.get("/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_book = crud.get_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.put("/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book: schemas.BookUpdate, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_book = crud.update_book(db=db, book_id=book_id, book_update=book)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book

@router.delete("/{book_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(book_id: int, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    db_book = crud.delete_book(db=db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")