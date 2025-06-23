from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class AuthorCreate(BaseModel):
    fullname: str
    bio: Optional[str] 
    avatar: Optional[str] 

class AuthorListResponse(BaseModel):
    id: int
    fullname: Optional[str]
    bio: Optional[str]
    avatar: Optional[str]
    created_at: datetime
    updated_at: datetime

class AuthorUpdate(BaseModel):
    fullname: Optional[str] = None
    bio: Optional[str] = None
    avatar: Optional[str] = None