from fastapi import APIRouter, HTTPException, Response
from app.depends.dependencies import db_dep
from app.models.models import Tag
from app.schemas.tag import TagCreate, TagUpdate, TagResponse

router = APIRouter(
    prefix="/tag",
    tags=["tag"]
)

@router.get("/", response_model=list[TagResponse])
async def get_all(db: db_dep):
    tags = db.query(Tag).all()

    if not tags:
        raise HTTPException(status_code=404, detail="Tags not found")
    return tags


@router.get("/{tag_id}", response_model=TagResponse)
async def get_tag(tag_id: int, db: db_dep):
    tag = db.query(Tag).filter(Tag.id == tag_id).first()

    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


@router.post("/create/", response_model=TagResponse, status_code=201)
async def create_tag(request: TagCreate, db: db_dep):
    new_tag = Tag(**request.model_dump())

    db.add(new_tag)
    db.commit()
    db.refresh(new_tag)
    return new_tag


@router.put("/{tag_id}/update/", response_model=TagResponse)
async def update_tag(tag_id: int, request:TagUpdate, db: db_dep):
    tag_obj = db.query(Tag).filter(Tag.id == tag_id).first()

    if not tag_obj:
        raise HTTPException(status_code=404, detail="Tag not found" )
    
    tag_obj.name = request.name
    db.commit()
    db.refresh(tag_obj)
    return tag_obj

@router.delete("/{tag_id}/delete/", status_code=204)
async def delete_tag(tag_id: int, db: db_dep):
    tag_obj = db.query(Tag).filter(Tag.id == tag_id).first()

    if not tag_obj:
        raise HTTPException(status_code=404, detail="Tag not found ")
    
    db.delete(tag_obj)
    db.commit()
    return Response(status_code=204)