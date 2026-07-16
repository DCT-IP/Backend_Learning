# main.py
from fastapi import FastAPI, HTTPException, status, Response, Query
from typing import Optional
from database import db
from models import Book

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Book API!"}

@app.get("/books", response_model=list[Book])
def get_all_books(
    author: Optional[str] = Query(None, description="Filter books by author"),
    max_price: Optional[float] = Query(None, description="Filter books costing up to this price")
):
    results = db
    
    if author:
        results = [b for b in results if author.lower() in b.author.lower()]
        
    if max_price is not None:
        results = [b for b in results if b.price <= max_price]
        
    return results

@app.get("/books/{id}", response_model=Book)
def get_book_by_id(id: int):
    for book in db:
        if book.id == id:
            return book
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Book with id {id} not found"
    )

@app.post("/books", response_model=Book, status_code=status.HTTP_201_CREATED)
def create_book(book: Book):
    if any(b.id == book.id for b in db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Book with id {book.id} already exists"
        )
    
    db.append(book)
    return book

@app.put("/books/{id}", response_model=Book)
def update_book(id: int, updated_book: Book):
    if updated_book.id != id:
        updated_book.id = id

    for index, book in enumerate(db):
        if book.id == id:
            db[index] = updated_book
            return updated_book
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Book with id {id} not found"
    )

@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_book(id: int):
    for index, book in enumerate(db):
        if book.id == id:
            db.pop(index)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
            
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail=f"Book with id {id} not found"
    )