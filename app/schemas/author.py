from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone


class AuthorCreate(BaseModel):
    fullname: str
    bio: Optional[str] = None
    avatar: Optional[str] = None
    updated_at: Optional[datetime] = datetime.now(timezone.utc)

class AuthorResponse(BaseModel):
    id: int
    created_at: Optional[datetime] = datetime.now(timezone.utc)
    fullname: str
    bio: Optional[str] = None
    avatar: Optional[str] = None
    updated_at: Optional[datetime] = datetime.now(timezone.utc)

    