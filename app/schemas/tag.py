from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TagBase(BaseModel):
    name: str

class TagCreate(TagBase):
    pass 

class TagUpdate(TagBase):
    pass 

class TagResponse(TagBase):
    id: int