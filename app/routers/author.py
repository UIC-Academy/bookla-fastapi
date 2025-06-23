from fastapi import APIRouter, HTTPException, Response
from typing import List
from app.models import Author
from app.schemas.author import AuthorCreate, AuthorResponse
from app.dependencies import db_dep


router = APIRouter(prefix="/author", tags=["author"])


@router.get("/", response_model=List[AuthorResponse])
async def list_authors(db: db_dep):
    authors = db.query(Author).all()
    if not authors:
        raise HTTPException(status_code=404, detail="Authorlar topilmadi")
    return authors



@router.get("/{author_id}", response_model=AuthorResponse)
async def get_author(author_id: int, db: db_dep):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author topilmadi")
    return author


@router.post("/create/", response_model=AuthorResponse)
async def create_author(author: AuthorCreate, db: db_dep):
    new_author = Author(**author.model_dump())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author



@router.put("/{author_id}/update/", response_model=AuthorResponse)
async def update_author(author_id: int, author: AuthorCreate, db: db_dep):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author topilmadi")
    for key, value in author.model_dump().items():
        setattr(db_author, key, value)

    db.commit()
    db.refresh(db_author)
    return db_author



@router.delete("/{author_id}/delete/")
async def del_author(author_id: int, db: db_dep):
    delete_author = db.query(Author).filter(Author.id == author_id).first()
    if not delete_author:
        raise HTTPException(status_code=404, detail="O'chirishga author topilmadi")
    db.delete(delete_author)
    db.commit()
    return Response(status_code=204)


