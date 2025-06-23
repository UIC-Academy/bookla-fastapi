from fastapi import APIRouter, HTTPException, Response
from app.schemas.book import BookCreate, BookResponse
from app.dependencies import db_dep
from app.models import Book
from typing import List


router = APIRouter(prefix="/book", tags=["book"])


@router.get("/", response_model=List[BookResponse])
async def list_books(db: db_dep):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")
    return books


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: db_dep):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/create/", response_model=BookCreate)
async def create_book(book: BookCreate, db: db_dep):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book


@router.put("/{book_id}/update/", response_model=BookCreate)
async def update_book(book_id: int, book: BookCreate, db: db_dep):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    for key, value in book.model_dump().items():
        setattr(db_book, key, value)

    db.commit()
    db.refresh(db_book)
    return db_book


@router.delete("/{book_id}/delete/")
async def del_book(book_id: int, db: db_dep):
    delete_book = db.query(Book).filter(Book.id == book_id).first()
    if not delete_book:
        raise HTTPException(status_code=404, detail="Book not found")
    db.delete(delete_book)
    db.commit()
    return Response(status_code=204)

