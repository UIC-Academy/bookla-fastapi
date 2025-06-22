from fastapi import APIRouter, HTTPException, Response
from app.depends.dependencies import db_dep
from app.models.models import Author
from app.schemas.author import AuthorCreate, AuthorUpdate, AuthorResponse



router = APIRouter(
    prefix="/author",
    tags=["author"]
)

@router.get("/", response_model=list[AuthorResponse])
async def get_all(db: db_dep):
    authors = db.query(Author).all()
    if not authors:
        raise HTTPException(status_code=404, detail="Authors not found")
    return authors


@router.get("/{author_id}", response_model=AuthorResponse)
async def get_author(author_id: int, db: db_dep):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    return author


@router.post("/create/", response_model=AuthorResponse, status_code=201)
async def create_author(request: AuthorCreate, db: db_dep):
    new_author = Author(**request.model_dump())

    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author


@router.put("/{author_id}/update/", response_model=AuthorResponse)
async def update_author(author_id: int, request: AuthorUpdate, db: db_dep):
    author_obj = db.query(Author).filter(Author.id == author_id).first()
    if not author_obj:
        raise HTTPException(status_code=404, detail="Author not found")
    
    
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(author_obj, key, value)
        
    db.commit()
    db.refresh(author_obj)
    return author_obj


@router.delete("/{author_id}/delete/", status_code=204)
async def delete_author(author_id: int, db: db_dep):
    author_obj = db.query(Author).filter(Author.id == author_id).first()
    if not author_obj:
        raise HTTPException(status_code=404, detail="Author not found")
    
    db.delete(author_obj)
    db.commit()
    return Response(status_code=204)
    




