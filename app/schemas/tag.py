from pydantic import BaseModel, Field
from typing import Optional

class TagCreate(BaseModel):
    name: str
    

class TagResponse(BaseModel):
    id: int
    name: Optional[str]