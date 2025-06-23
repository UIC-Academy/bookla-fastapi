from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class PublisherCreate(BaseModel):
    name: str
    location_url: str
    website_url: str 
    created_at: Optional[datetime] = datetime.now(datetime.timezone.utc) 


class PublisherResponse(BaseModel):
    id: int
    created_at: str
    name: str
    
    

    