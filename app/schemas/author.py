from pydantic import BaseModel
from typing import Optional


class AuthorCreate(BaseModel):
    full_name: str
    bio: Optional[str]
    avatar: Optional[str]
    

class AuthorListResponse(BaseModel):
    id: int
    full_name: str
    bio: Optional[str] = None
    avatar: Optional[str] = None
    