from fastapi import APIRouter, HTTPException
from app.dependencies import db_dep
from app.models import Tag
from app.schemas import TagResponse, TagCreate


router = APIRouter(
    prefix="/tag",
    tags=["tag"]
)

@router.get("/", response_model=list[TagResponse])
async def list_tags(db: db_dep):
    tags = db.query(Tag).all()
    if not tags:
        raise HTTPException(status_code=404, detail="Tag topilmadi !")
    return tags

@router.get("/{id}", response_model=TagResponse)
async def get_tag(id: int, db: db_dep):
    tag = db.query(Tag).filter(Tag.id == id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag topilmadi !")
    return tag  

@router.post("/create/", response_model=TagResponse)
async def create_tag(tag: TagCreate, db: db_dep):
    new_tag = Tag(**tag.model_dump())
    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag

@router.put("/{id}/update/", response_model=TagResponse)
async def update_tag(id: int, tag: TagCreate, db: db_dep):
    tag_obj = db.query(Tag).filter(Tag.id == id).first()
    if not tag_obj:
        raise HTTPException(status_code=404, detail="Tag topilmadi !")
    
    tag_obj.name = tag.name
    db.commit()
    db.refresh(tag_obj)
    return tag_obj   

@router.delete("/{id}/delete/", response_model=dict)
async def delete_tag(id: int, db: db_dep):
    tag = db.query(Tag).filter(Tag.id == id).first()
    if not tag:
        raise HTTPException(status_code=404, detail="Tag topilmadi !")

    db.delete(tag)
    db.commit()
    return {"detail": "Tag ochirildi !"}