from pydantic import BaseModel
from typing import Optional


class BookCreate(BaseModel):

    name: str
    description: Optional[str]
    isbn: str
    cover: Optional[str]
    page_count: int
    rating: float


class BookListResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    isbn: str
    cover: Optional[str] = None
    page_count: int
    rating: float
    
