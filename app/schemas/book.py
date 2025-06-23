from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional

class BookCreate(BaseModel):
    name: str
    description: str
    isbn: str
    cover:str
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    rating: float
    is_active: bool
    updated_at: Optional[datetime] =datetime.now(timezone.utc)

class BookResponse(BaseModel):
    id: int
    created_at: datetime
    name: str
    description: str
    isbn: str
    cover: str
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    rating: float
    is_active: bool
    updated_at: Optional[datetime] = datetime.now(timezone.utc)
    

   