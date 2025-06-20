from fastapi import APIRouter, HTTPException, Response
from app.depends.dependencies import db_dep, pagination_dep
from app.models.models import Publisher
from app.schemas.publisher import PublisherCreate, PublisherUpdate, PublisherResponse


router = APIRouter(
    prefix="/publisher",
    tags=["publisher"]
)

@router.get("/", response_model=list[PublisherResponse])
async def get_all(db: db_dep):
    publishers = db.query(Publisher).all()
    if not publishers:
        raise HTTPException(status_code=404, detail="Publishers not found")
    return publishers


@router.get("/{publisher_id}", response_model=PublisherResponse)
async def get_publisher(publisher_id: int, db: db_dep):
    publisher = db.query(Publisher).filter(Publisher.id == publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher


@router.post("/create/", response_model=PublisherResponse, status_code=201)
async def create_publisher(request: PublisherCreate, db: db_dep):
    new_publisher = Publisher(**request.model_dump())

    db.add(new_publisher)
    db.commit()
    db.refresh(new_publisher)
    return new_publisher


@router.put("/{publisher_id}/update/", response_model=PublisherResponse)
async def update_publisher(publisher_id: int, request: PublisherUpdate, db: db_dep):
    publisher_obj = db.query(Publisher).filter(Publisher.id == publisher_id).first()

    if not publisher_id:
        raise HTTPException(status_code=404, detail="Publisher not found")
    
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(publisher_obj, key, value)
        
    db.commit()
    db.refresh(publisher_obj)
    return publisher_obj

@router.delete("/{publisher_id}/delete/", status_code=204)
async def delete_publisher(publisher_id: int, db: db_dep):
    publisher_obj = db.query(Publisher).filter(Publisher.id == publisher_id).first()

    if not publisher_obj:
        raise HTTPException(status_code=404, detail="Publisher not found")
    
    db.delete(publisher_obj)
    db.commit()
    return Response(status_code=204)

@router.patch("/{publisher_id}", response_model=PublisherResponse)
async def change_publisher(publisher_id: int, request: PublisherUpdate, db: db_dep):
    publisher_obj = db.query(Publisher).filter(Publisher.id == publisher_id).first()

    if not publisher_obj:
        raise HTTPException(status_code=404, detail="Publisher not found")

    update_data = request.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(publisher_obj, key, value)

    db.commit()
    db.refresh(publisher_obj)
    return publisher_obj




