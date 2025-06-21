from fastapi import APIRouter, HTTPException, Response

from app.depends.dependencies import db_dep, pagination_dep
from app.models.models import Book, Tag
from app.schemas.book import BookCreate, BookUpdate, BookResponse
from typing import List


router = APIRouter(
    prefix="/book",
    tags=["book"]
)


@router.get("/", response_model=List[BookResponse])
async def get_all(db: db_dep):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="Sorry, Books not found")
    return books


@router.get("/{book_id}", response_model=BookResponse)
async def get_book(book_id: int, db: db_dep):
    get_book_by_id = db.query(Book).filter(Book.id == book_id).first()

    if not get_book_by_id:
        raise HTTPException(status_code=404, detail="Sorry, Book not found")
    return get_book_by_id


@router.post("/create/", response_model=BookResponse, status_code=201)
async def create_book(request: BookCreate, db: db_dep):
    tag_objs = db.query(Tag).filter(Tag.id.in_(request.tags or [])).all()

    new_book = Book(**request.model_dump(exclude={"tags"}))
    new_book.tags = tag_objs

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book



@router.put("/{book_id}/update/", response_model=BookResponse)
async def update_book(book_id: int, request: BookUpdate, db: db_dep):
    update_book_by_id = db.query(Book).filter(Book.id == book_id).first()
    if not update_book_by_id:
        raise HTTPException(status_code=404, detail="Sorry, Book not found")

    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(update_book_by_id, key, value)

    db.commit()
    db.refresh(update_book_by_id)
    return update_book_by_id


@router.delete("/{book_id}/delete/", status_code=204)
async def delete_book(book_id: int, db: db_dep):
    delete_book_by_id = db.query(Book).filter(Book.id == book_id).first()

    if not delete_book_by_id:
        raise HTTPException(status_code=404, detail="Sorry, Book not found")
    
    db.delete(delete_book_by_id)
    db.commit()
    return Response(status_code=204)
