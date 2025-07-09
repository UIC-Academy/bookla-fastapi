from pydantic import BaseModel
from typing import Optional, List

from datetime import datetime

from app.schemas import TagListResponse


class BookCreate(BaseModel):
    name: str
    description: Optional[str] = None
    isbn: str
    cover: Optional[str] | None = None
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    tags: List[int] | None = None


class BookListResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    isbn: str
    tags: List[TagListResponse] = None
    created_at: datetime
    updated_at: datetime
