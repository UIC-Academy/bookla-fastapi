from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timezone


class PublisherCreate(BaseModel):
    name: str
    location_url: Optional[str]
    website_url: Optional[str]
    updated_at: Optional[datetime] = datetime.now(timezone.utc)


class PublisherResponse(BaseModel):
    id: int
    created_at: Optional[datetime] = datetime.now(timezone.utc)
    name: str
    location_url: Optional[str]
    website_url: Optional[str]
    updated_at: Optional[datetime] = datetime.now(timezone.utc)
    
