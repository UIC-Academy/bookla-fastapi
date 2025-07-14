from fastapi import APIRouter, HTTPException

from app.dependencies import db_dep
from app.models import Book, Tag
from app.schemas.book import BookCreate, BookListResponse

router = APIRouter(
    prefix="/book",
    tags=["book"],
)


@router.get("/", response_model=list[BookListResponse])
async def list_book(db: db_dep):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    return books


@router.get("/{book_id}/", response_model=BookListResponse)
async def get_book(book_id: int, db: db_dep):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@router.post("/create/", response_model=BookListResponse)
async def create_book(book: BookCreate, db: db_dep):
    book_data = book.model_dump(exclude={"tags"})
    tag_ids = book.tags or []

    tags = db.query(Tag).filter(Tag.id.in_(tag_ids)).all()

    new_book = Book(**book_data, tags=tags)

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


@router.put("/{book_id}/update/", response_model=BookListResponse)
async def update_book(book_id: int, book: BookCreate, db: db_dep):
    book_obj = db.query(Book).filter(Book.id == book_id).first()
    if not book_obj:
        raise HTTPException(status_code=404, detail="Book not found")

    tag_ids = book.tag_ids or []
    book_data = book.model_dump(exclude={"tag_ids"})

    for field, value in book_data.items():
        setattr(book_obj, field, value)

    # Update tags
    if tag_ids:
        book_obj.tags.clear()
        for tag_id in tag_ids:
            tag = db.query(Tag).filter(Tag.id == tag_id).first()
            if tag:
                book_obj.tags.append(tag)

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
    return {"message": "Book deleted successfully"}
