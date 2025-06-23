from fastapi import APIRouter, HTTPException, Response
from app.dependencies import db_dep
from app.schemas import BookTagM2MCreate,BookTagM2MResponse, BookTagM2MUpdate, BookTagGroupResponse
from app.models import Tag, BookTagM2M, Book

router = APIRouter(
    prefix="/booktagm2m",
    tags=["booktagm2m"]
)

@router.get("/book-tags/group-by-books", response_model=BookTagGroupResponse, status_code=200)
async def group_by_book(db: db_dep):
    result = db.query(BookTagM2M.book_id, BookTagM2M.tag_id).all()

    group = {}

    for book_id, tag_id in result:
        group.setdefault(book_id, []).append(tag_id)
    
    return group

@router.get("/book-tags/group-by-tags", response_model=BookTagGroupResponse, status_code=200)
async def group_by_tag(db: db_dep):
    result = db.query(BookTagM2M.book_id, BookTagM2M.tag_id).all()

    group = {}

    for book_id, tag_id in result:
        group.setdefault(tag_id, []).append(book_id)
    
    return group

@router.post("/create/", response_model=BookTagM2MResponse,status_code=201)
async def create_booktagm2m(book_tag: BookTagM2MCreate, db: db_dep):
    new_book_tag = BookTagM2M(**book_tag.model_dump())

    bookid = db.query(Book).filter(Book.id == book_tag.book_id).first()
    if not bookid:
        raise HTTPException(status_code=404, detail="book_id not found")
    
    tagid = db.query(Tag).filter(Tag.id == book_tag.tag_id).first()
    if not tagid:
        raise HTTPException(status_code=404, detail="tag_id not found")
    
    db.add(new_book_tag)
    db.commit()
    db.refresh(new_book_tag)
    return new_book_tag



    

