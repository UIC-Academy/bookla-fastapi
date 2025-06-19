from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class PublisherBase(BaseModel):
    name: str
    location_url: Optional[str]
    website_url: Optional[str]

class PublisherCreate(PublisherBase):
    pass

class PublisherUpdate(PublisherBase):
    pass  

class PublisherResponse(PublisherBase):
    id: int
    created_at: datetime
    updated_at: datetime


