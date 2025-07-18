from fastapi import APIRouter, HTTPException

from app.dependencies import db_dep
from app.models import Tag
from app.schemas.tag import TagCreate, TagListResponse

router = APIRouter(
    prefix="/tag",
    tags=["tag"],
)


@router.get("/", response_model=list[TagListResponse])
async def list_tag(db: db_dep):
    tags = db.query(Tag).all()
    if not tags:
        raise HTTPException(status_code=404, detail="No tags found")
    return tags


@router.get("/{tag_id}/", response_model=TagListResponse)
async def get_tag(tag_id: int, db: db_dep):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@router.post("/create/", response_model=TagListResponse)
async def create_tag(tag: TagCreate, db: db_dep):
    new_tag = Tag(**tag.model_dump())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag


@router.put("/{tag_id}/update/", response_model=TagListResponse)
async def update_tag(tag_id: int, tag: TagCreate, db: db_dep):
    tag_obj = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag_obj:
        raise HTTPException(status_code=404, detail="Tag not found")

    for field, value in tag.model_dump().items():
        setattr(tag_obj, field, value)

    db.commit()
    db.refresh(tag_obj)
    return tag_obj


@router.delete("/{tag_id}/delete/")
async def delete_tag(tag_id: int, db: db_dep):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    db.delete(tag)
    db.commit()
    return {"message": "Tag deleted successfully"}
