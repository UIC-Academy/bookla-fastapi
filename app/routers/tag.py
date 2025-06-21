from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.tag import TagCreate, TagRead
from app.crud import tag as crud_tag
from app.database import get_db
from typing import List

router = APIRouter(prefix="/tags", tags=["Tags"])

@router.post("/", response_model=TagRead)
def create_tag(tag: TagCreate, db: Session = Depends(get_db)):
    return crud_tag.create_tag(db, tag)

@router.get("/", response_model=List[TagRead])
def read_tags(db: Session = Depends(get_db)):
    return crud_tag.get_all_tags(db)

@router.get("/{tag_id}", response_model=TagRead)
def read_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = crud_tag.get_tag(db, tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag

@router.put("/{tag_id}", response_model=TagRead)
def update_tag(tag_id: int, tag: TagCreate, db: Session = Depends(get_db)):
    updated = crud_tag.update_tag(db, tag_id, tag)
    if not updated:
        raise HTTPException(status_code=404, detail="Tag not found")
    return updated

@router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    deleted = crud_tag.delete_tag(db, tag_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Tag not found")
    return {"message": "Tag deleted"}
