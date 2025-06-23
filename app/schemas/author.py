from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AuthorCreate(BaseModel):
    fullname: str
    bio: Optional[str] 

class AuthorResponse(BaseModel):
    id: int
    fullname: str
    created_at: datetime
    updated_at: datetime