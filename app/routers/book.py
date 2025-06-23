from fastapi import APIRouter, Depends, HTTPException

from app.dependencies import db_dep, pagination_dep
from app.models import Book
from app.schemas.book import BookCreate, BookResponse    


router = APIRouter(
    prefix="/book",
    tags=["book"]
)

@router.get("/", response_model=list[BookResponse])
async def list_books(db=Depends(db_dep)):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return books

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db=Depends(db_dep)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    return book

@router.post("/create/", response_model=BookResponse)  
async def create_book(book: BookCreate, db=Depends(db_dep)):
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/{book_id}/update/", response_model=BookResponse)    
async def update_book(book_id: int, book: BookCreate, db=Depends(db_dep)):
    book_obj = db.query(Book).filter(Book.id == book_id).first()
    if not book_obj:
        raise HTTPException(status_code=404, detail="Book not found")
    
    for key, value in book.model_dump().items():
        setattr(book_obj, key, value)
    
    db.commit()
    db.refresh(book_obj)
    return book_obj 

@router.delete("/{book_id}/delete/")
async def delete_book(book_id: int, db=Depends(db_dep)):    
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"detail": "Book deleted successfully"}
