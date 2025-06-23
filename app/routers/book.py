from fastapi import APIRouter, HTTPException, Response

from app.dependencies import db_dep
from app.models import Book
from app.schemas import BookCreate, BookListResponse


router = APIRouter(
    prefix = "/book",
    books= ["book"]
)

@router.get("/", response_model=list[BookListResponse])
async def list_book(db: db_dep):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return books

@router.get("/{book_id}", response_model=BookListResponse)
async def get_book(book_id: int, db: db_dep):
    book = db.query(Book).filter(Book.id == book_id).filter()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

@router.post("/create/", response_model=BookListResponse)
async def create_book(book: BookCreate, db: db_dep)
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/{book_id}/update/", response_model=BookListResponse)
async def update_book(book_id: int, book: BookCreate, db: db_dep):
    book_obj= db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book_obj.name = book.name
    book_obj.description = book.description
    book_obj.isbn = book.isbn
    book_obj.cover = book.cover
    book_obj.page_count = book.page_count
    book_obj.rating = book.rating
    db.commit()
    db.refresh(book_obj)
    return book_obj

@router.delete("/{book_id}/delete/")
async def delete_book(book_id: int, db: db_dep):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return Response(status_code=204)

