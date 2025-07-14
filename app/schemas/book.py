from datetime import datetime

from pydantic import BaseModel

from app.schemas.tag import TagListResponse


class BookCreate(BaseModel):
    name: str
    description: str | None = None
    isbn: str
    cover: str | None | None = None
    page_count: int
    author_id: int
    category_id: int
    publisher_id: int
    tags: list[int] | None = None


class BookListResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    isbn: str
    cover: str | None = None
    tags: list[TagListResponse] = None
    created_at: datetime
    updated_at: datetime
