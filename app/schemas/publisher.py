from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PublisherCreate(BaseModel):
    name: str
    location_url: Optional[str]
    website_url: Optional[str]


class PublisherResponse(BaseModel):
    id: int
    created_at: datetime
    name: str
    location_url: Optional[str]
    website_url: Optional[str]
    updated_at: datetime
    
