from fastapi import APIRouter, HTTPException, Response
from app.dependencies import db_dep
from app.models import Author
from app.schemas import AuthorCreate, AuthorListResponse

router = APIRouter(
    prefix="/author",
    tags=["author"]
)

@router.get("/", response_model=list[AuthorListResponse])
async def list_author(db: db_dep):
    return db.query(Author).all()

@router.get("/{author_id}", response_model=AuthorListResponse)
async def get_author(author_id: int, db: db_dep):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author

@router.post("/create/", response_model=AuthorListResponse)
async def create_author(author: AuthorCreate, db: db_dep):
    new_author = Author(**author.model_dump())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.put("/{author_id}/update/", response_model=AuthorListResponse)
async def update_author(author_id: int, author: AuthorCreate, db: db_dep):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    db_author.name = author.name
    db.commit()
    db.refresh(db_author)
    return db_author

@router.delete("/{author_id}/delete/")
async def delete_author(author_id: int, db: db_dep):
    db_author = db.query(Author).filter(Author.id == author_id).first()
    if not db_author:
        raise HTTPException(status_code=404, detail="Author not found")
    db.delete(db_author)
    db.commit()
    return Response(status_code=204)
