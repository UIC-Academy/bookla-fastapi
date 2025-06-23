from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    name: str
    description: Optional[str] = None
    isbn: str
    cover: Optional[str] = None
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    rating: float = 0.0
    is_active: bool = True

class BookUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    isbn: Optional[str] = None
    cover: Optional[str] = None
    page_count: Optional[int] = None
    author_id: Optional[int] = None
    category_id: Optional[int] = None
    publisher_id: Optional[int] = None
    rating: Optional[float] = None
    is_active: Optional[bool] = None

class BookListResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    isbn: str
    cover: Optional[str] = None
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    rating: float = 0.0
    is_active: bool = True

class BookDictResponse(BaseModel):
    total_count: int
    books: list[BookListResponse]

