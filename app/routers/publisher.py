from fastapi import APIRouter, HTTPException

from app.dependencies import db_dep
from app.models import Publisher
from app.schemas.publisher import PublisherCreate, PublisherListResponse

router = APIRouter(
    prefix="/publisher",
    tags=["publisher"],
)


@router.get("/", response_model=list[PublisherListResponse])
async def list_publisher(db: db_dep):
    publishers = db.query(Publisher).all()
    if not publishers:
        raise HTTPException(status_code=404, detail="No publishers found")
    return publishers


@router.get("/{publisher_id}", response_model=PublisherListResponse)
async def get_publisher(publisher_id: int, db: db_dep):
    publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher


@router.post("/create/", response_model=PublisherListResponse)
async def create_publisher(publisher: PublisherCreate, db: db_dep):
    new_publisher = Publisher(**publisher.model_dump())
    db.add(new_publisher)
    db.commit()
    db.refresh(new_publisher)
    return new_publisher


@router.put("/{publisher_id}/update/", response_model=PublisherListResponse)
async def update_publisher(publisher_id: int, publisher: PublisherCreate, db: db_dep):
    publisher_obj = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not publisher_obj:
        raise HTTPException(status_code=404, detail="Publisher not found")

    for field, value in publisher.model_dump().items():
        setattr(publisher_obj, field, value)

    db.commit()
    db.refresh(publisher_obj)
    return publisher_obj


@router.delete("/{publisher_id}/delete/")
async def delete_publisher(publisher_id: int, db: db_dep):
    publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")

    db.delete(publisher)
    db.commit()
    return {"message": "Publisher deleted successfully"}
