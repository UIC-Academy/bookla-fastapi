from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional

class AuthorCreate(BaseModel):
    name: str
    bio: Optional[str] = None
    avatar: Optional[str] = None
    updated_at: Optional[datetime] = datetime.now(timezone.utc)

class AuthorResponse(BaseModel):
    id:int
    created_at: datetime
    full_name: str
    bio: Optional[str] = None
    avatar: Optional[str] = None
    updated_at: Optional[datetime] = datetime.now(timezone.utc)
    
