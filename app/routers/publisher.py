from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.database import get_db
from app.schemas import PublisherCreate, PublisherResponse, PublisherUpdate
from app.crud import publisher as publisher_crud

router = APIRouter(prefix="/publishers", tags=["Publishers"])


@router.post("/", response_model=PublisherResponse)
async def create_publisher(schema: PublisherCreate, db: AsyncSession = Depends(get_db)):
    return await publisher_crud.create_publisher(db, schema)


@router.get("/", response_model=List[PublisherResponse])
async def list_publishers(db: AsyncSession = Depends(get_db)):
    return await publisher_crud.get_all_publishers(db)


@router.get("/{publisher_id}", response_model=PublisherResponse)
async def get_publisher(publisher_id: int, db: AsyncSession = Depends(get_db)):
    publisher = await publisher_crud.get_publisher_by_id(db, publisher_id)
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return publisher


@router.put("/{publisher_id}", response_model=PublisherResponse)
async def update_publisher(publisher_id: int, schema: PublisherUpdate, db: AsyncSession = Depends(get_db)):
    updated = await publisher_crud.update_publisher(db, publisher_id, schema)
    if not updated:
        raise HTTPException(status_code=404, detail="Publisher not found")
    return updated


@router.delete("/{publisher_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_publisher(publisher_id: int, db: AsyncSession = Depends(get_db)):
    success = await publisher_crud.delete_publisher(db, publisher_id)
    if not success:
        raise HTTPException(status_code=404, detail="Publisher not found")
