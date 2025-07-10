from pydantic import BaseModel


class PublisherCreate(BaseModel):
    name: str
    location_url: str | None = None
    website_url: str | None = None


class PublisherListResponse(BaseModel):
    id: int
    name: str
    location_url: str | None = None
    website_url: str | None = None
