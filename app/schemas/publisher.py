from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PublisherCreate(BaseModel):
    name: str
    location_url: Optional[str] 
    website_url: Optional[str] 

class PublisherResponse(BaseModel):
    id: int
    name: str
    location_url: Optional[str] = None
    website_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
