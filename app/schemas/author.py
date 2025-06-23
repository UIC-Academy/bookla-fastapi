from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class AuthorCreate(BaseModel):
    fullname: str
    bio: Optional[str] = None
    avatar: Optional[str] = None

class AuthorResponse(BaseModel):
    id: int
    created_at: datetime
    fullname: str
    bio: Optional[str] = None
    avatar: Optional[str] = None
    updated_at: datetime

    