from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PublisherCreate(BaseModel):
    name: str
    location_url: Optional[str]
    website_url: Optional[str]

class PublisherListResponse(BaseModel):
    id: int
    name: str
    location_url: Optional[str] = None
    website_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime

class PublisherUpdate(BaseModel):
    name: Optional[str] = None
    location_url: Optional[str] = None
    website_url: Optional[str] = None

    # class Config:
    #     orm_mode = True
    #     allow_population_by_field_name = True
    #     use_enum_values = True
    #     json_encoders = {
    #         datetime: lambda v: v.isoformat() if v else None
    #     }