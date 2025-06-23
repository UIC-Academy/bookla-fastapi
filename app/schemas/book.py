from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class BookCreate(BaseModel):
    name: str
    description: Optional[str] = None
    isbn: str
    cover: Optional[str] = None
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    is_active: Optional[bool] = True
    

class BookResponse(BaseModel):
    id: int
    created_at: datetime
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
    updated_at: datetime


