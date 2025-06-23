from pydantic import BaseModel

class PublisherCreate(BaseModel):
    name: str

class PublisherResponse(BaseModel):
    id: int
    created_at: str
    name: str
    location_url: str
    website_url: str
    updated_at: str
    

    