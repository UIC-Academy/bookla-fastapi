from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, timezone

class BookCreate(BaseModel):
    name: str
    description: Optional[str] = None
    isbn: str
    cover: Optional[str] = None
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    rating: float
    is_active: Optional[bool] = True
    updated_at: Optional[datetime] = datetime.now(timezone.utc)
    

class BookResponse(BaseModel):
    id: int
    created_at: Optional[datetime] = datetime.now(timezone.utc)
    name: str
    description: Optional[str] = None
    isbn: str
    cover: Optional[str] = None
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    rating: float
    is_active: Optional[bool] = True
    updated_at: Optional[datetime] = datetime.now(timezone.utc)

