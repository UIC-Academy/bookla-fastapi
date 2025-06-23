from fastapi import APIRouter, HTTPException
from app.dependencies import db_dep
from app.models import Book
from app.schemas import BookCreate, BookResponse, BookUpdate

router = APIRouter(
    prefix="/book",
    tags=["book"]
)

@router.post("/", response_model=BookResponse)
async def create_book(book: BookCreate, db: db_dep):
    db_book = Book(**book.model_dump())
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

@router.get("/", response_model=list[BookResponse])
async def list_books(db: db_dep):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="Kitob topilmadi !")
    return books                                                

@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: db_dep):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Kitob topilmadi !")
    return book

@router.put("/{book_id}", response_model=BookResponse)          
async def update_book(book_id: int, book: BookUpdate, db: db_dep):
    db_book = db.query(Book).filter(Book.id == book_id).first()
    if not db_book:
        raise HTTPException(status_code=404, detail="Kitob topilmadi !")
    
    for key, value in book.model_dump(exclude_unset=True).items():
        setattr(db_book, key, value)
    
    db.commit()
    db.refresh(db_book)
    return db_book

@router.delete("/{book_id}")
async def delete_book(book_id: int, db: db_dep):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Kitob topilmadi !")
    
    db.delete(book)
    db.commit()
    return {"detail": "Kitob o'chirildi !"}