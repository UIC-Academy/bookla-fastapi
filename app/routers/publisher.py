from fastapi import APIRouter, HTTPException, Response
from typing import List
from app.dependencies import db_dep, pagination_dep
from app.models import Publisher
from app.schemas.publisher import PublisherCreate, PublisherResponse

router = APIRouter(prefix="/publisher", tags=["publisher"])


@router.get("/", response_model=List[PublisherResponse])
async def list_publisher(db: db_dep):
    publishers = db.query(Publisher).all()
    if not publishers:
        raise HTTPException(status_code=404, detail="Publisherlar topilmadi")
    return publishers


@router.get("/{publisher_id}", response_model=PublisherResponse)
async def get_publisher(publisher_id: int, db: db_dep):
    publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher topilmadi")
    return publisher


@router.post("/create/", response_model=PublisherResponse)
async def create_publisher(publisher: PublisherCreate, db: db_dep):
    new_publisher = Publisher(**publisher.model_dump())
    db.add(new_publisher)
    db.commit()
    db.refresh(new_publisher)
    return new_publisher


@router.put("/{publisher_id}/update/", response_model=PublisherResponse)
async def update_publisher(publisher_id: int, publisher: PublisherCreate, db: db_dep):
    db_publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not db_publisher:
        raise HTTPException(status_code=404, detail="Publisher topilmadi")
    
    for key, value in publisher.model_dump().items():
        setattr(db_publisher, key, value)

    db.commit()
    db.refresh(db_publisher)
    return db_publisher


@router.delete("/{publisher_id}/delete/")
async def delete_publisher(publisher_id: int, db: db_dep):
    del_publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not del_publisher:
        raise HTTPException(status_code=404, detail="O'chirishga Publisher topilmadi")
    
    db.delete(del_publisher)
    db.commit()
    return Response(status_code=204)
