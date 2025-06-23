from fastapi import APIRouter, HTTPException, Response

from app.dependencies import db_dep, pagination_dep
from app.models import Tag
from app.schemas import TagCreate, TagListResponse

router = APIRouter(
    tags=["tag"]
)

@router.get("/tags/", response_model=list[TagListResponse], status_code=200)
async def list_tag(db: db_dep):
    tags = db.query(Tag).all()
    if not tags:
        raise HTTPException(status_code=404, detail="No tags found")
    
    return tags

@router.get("/tag/{tag_id}", response_model=TagListResponse, status_code=200)
async def get_tag(tag_id: int, db: db_dep):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    return tag

@router.post("/tag/create/", response_model=TagListResponse, status_code=201)
async def create_tag(tag: TagCreate, db: db_dep):
    new_tag = Tag(**tag.model_dump())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

@router.put("/tag/{tag_id}/update/", response_model=TagListResponse, status_code=200)
async def update_tag(tag_id: int, tag: TagCreate, db: db_dep):
    tag_obj = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag_obj:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    tag_obj.name = tag.name
    db.commit()
    db.refresh(tag_obj)
    return tag_obj

@router.delete("/tag/{tag_id}/delete/", status_code=204)
async def delete_tag(tag_id: int, db: db_dep):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    
    db.delete(tag)
    db.commit()


