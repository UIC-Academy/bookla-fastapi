from pydantic import BaseModel
from typing import Optional


class AuthorCreate(BaseModel):
    fullname: str
    bio: Optional[str] = None
    avatar: Optional[str] = None


class AuthorListResponse(BaseModel):
    id: int
    fullname:str
    bio: Optional[str] = None
    avatar: Optional[str] = None
