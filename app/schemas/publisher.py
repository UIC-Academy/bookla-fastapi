from pydantic import BaseModel
from typing import Optional


class PublisherCreate(BaseModel):

    name: str
    location_url: Optional[str]
    website_url: Optional[str]

class PublisherListResponse(BaseModel):

    id: int
    name: str
    location_url: Optional[str]= None
    website_url: Optional[str]= None