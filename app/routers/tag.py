from fastapi import APIRouter, HTTPException, Response
from typing import List
from app.models import Tag
from app.dependencies import db_dep
from app.schemas.tag import TagCreate, TagResponse

router = APIRouter(prefix="/tag", tags=["tag"])


@router.get("/", response_model=List[TagResponse])
async def list_tags(db: db_dep):
    tags = db.query(Tag).all()
    if not tags:
        raise HTTPException(status_code=404, detail="Tag topilmadi")
    return tags


@router.get("/{tag_id}", response_model=TagResponse)
async def get_tag(tag_id: int, db: db_dep):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag topilmadi")
    return tag


@router.post("/create/", response_model=TagResponse)
async def create_tag(tag: TagCreate, db: db_dep):
    new_tag = Tag(**tag.model_dump())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag


@router.put("/{tag_id}/update/", response_model=TagResponse)
async def update_tag(tag_id: int, tag: TagCreate, db: db_dep):
    db_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not db_tag:
        raise HTTPException(status_code=404, detail="Tag topilmadi")
    
    for key, value in tag.model_dump().items():
        setattr(db_tag, key, value)

    db.commit()
    db.refresh(db_tag)
    return db_tag


@router.delete("/{tag_id}/delete/")
async def del_tag(tag_id: int, db: db_dep):
    del_tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not del_tag:
        raise HTTPException(status_code=404, detail="Tag topilmadi")
    
    db.delete(del_tag)
    db.commit()
    return Response(status_code=204)
