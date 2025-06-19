from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AuthorBase(BaseModel):
    fullname: str
    bio: Optional[str]
    avatar: Optional[str]

class AuthorCreate(AuthorBase):
    pass 

class AuthorUpdate(BaseModel):
    fullname: Optional[str]
    bio: Optional[str]
    avatar: Optional[str]


class AuthorResponse(AuthorBase):
    id: int
    created_at: datetime
    updated_at: datetime