from fastapi import APIRouter, HTTPException, Response
from app.dependencies import db_dep, pagination_dep
from app.schemas import AuthorCreate, AuthorListResponse, AuthorUpdate
from app.models import Author


router = APIRouter(
    prefix="/author",
    tags=["author"]
)

@router.get("/list/", response_model=list[AuthorListResponse], status_code=200)
async def list_authors(db: db_dep):
    authors = db.query(Author).all()
    if not authors:
        raise HTTPException(status_code=404, detail="No authors found")
    return authors

@router.get("/{id}", response_model=AuthorListResponse, status_code=200)
async def get_author_id(id: int, db: db_dep):
    author = db.query(Author).filter(Author.id == id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not fount")
    return author

@router.post("/create/", response_model=AuthorListResponse, status_code=201)
async def create_author(author: AuthorCreate, db: db_dep):
    new_author = Author(**author.model_dump())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.put("/update/{id}", response_model=AuthorListResponse, status_code=200)
async def update_author(id: int, author: AuthorUpdate, db: db_dep):
    author_obj = db.query(Author).filter(Author.id == id).first()
    if not author_obj:
        raise HTTPException(status_code=404, detail="Author not found")
    author_obj.fullname = author.fullname
    author_obj.bio = author.bio
    author_obj.avatar = author.avatar
    db.commit()
    db.refresh(author_obj)
    return author_obj

@router.patch("/update/{id}", response_model=AuthorUpdate, status_code=200)
async def update_author_1(id: int, author: AuthorUpdate, db: db_dep):
    author_obj = db.query(Author).filter(Author.id == id).first()
    if not author_obj:
        raise HTTPException(status_code=404, detail="Author not found")
    author_obj.fullname = author.fullname if author.fullname else author_obj.fullname
    author_obj.bio = author.bio if author.bio else author_obj.bio
    author_obj.avatar = author.avatar if author.avatar else author_obj.avatar
    db.commit()
    db.refresh(author_obj)
    return author_obj

@router.delete("/delete/{id}", status_code=204)
async def delete_author(id: int, db: db_dep):
    author = db.query(Author).filter(Author.id == id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(author)
    db.commit()