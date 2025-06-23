from fastapi import APIRouter, Depends, HTTPException
from app.dependencies import db_dep, pagination_dep
from app.models import Author
from app.schemas.author import AuthorCreate, AuthorResponse

router = APIRouter(
    prefix="/author",
    tags=["author"]
)

@router.get("/", response_model=list[AuthorResponse])
async def list_authors(db=Depends(db_dep)):
    authors = db.query(Author).all()
    if not authors:
        raise HTTPException(status_code=404, detail="No authors found")
    
    return authors

@router.get("/{author_id}", response_model=AuthorResponse)
async def get_author(author_id: int, db=Depends(db_dep)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    return author

@router.post("/create/", response_model=AuthorResponse)
async def create_author(author: AuthorCreate, db=Depends(db_dep)):
    new_author = Author(**author.model_dump())
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    return new_author

@router.put("/{author_id}/update/", response_model=AuthorResponse)
async def update_author(author_id: int, author: AuthorCreate, db=Depends(db_dep )):
    author_obj = db.query(Author).filter(Author.id == author_id).first()
    if not author_obj:
        raise HTTPException(status_code=404, detail="Author not found")
    
    for key, value in author.model_dump().items():
        setattr(author_obj, key, value)
    
    db.commit()
    db.refresh(author_obj)
    return author_obj

@router.delete("/{author_id}/delete/")
async def delete_author(author_id: int, db=Depends(db_dep)):
    author = db.query(Author).filter(Author.id == author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    db.delete(author)
    db.commit()
    return {"detail": "Author deleted successfully"}
