from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from app.schemas.tag import TagResponse


class BookCreate(BaseModel):
    name: str 
    description: Optional[str] = None
    isbn: str 
    cover: Optional[str] = None
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    tags: Optional[List[int]] = None  


class BookUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    isbn: Optional[str] = None
    cover: Optional[str] = None
    page_count: Optional[int] = None
    author_id: Optional[int] = None
    category_id: Optional[int] = None
    publisher_id: Optional[int] = None
    tags: Optional[List[int]] = None



class BookResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    isbn: str
    cover: Optional[str]
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    rating: float
    is_active: bool
    created_at: datetime
    updated_at: datetime
    tags: List[TagResponse]


