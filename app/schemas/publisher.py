from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class PublisherBase(BaseModel):
    name: str
    location_url: Optional[str]
    website_url: Optional[str]


class PublisherUpdate(BaseModel):
    name: Optional[str] =None
    location_url: Optional[str] = None
    website_url: Optional[str] = None


class PublisherCreate(PublisherBase):
    pass

class PublisherResponse(PublisherBase):
    id: int
    created_at: datetime
    updated_at: datetime


