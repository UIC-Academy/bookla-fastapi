from pydantic import BaseModel,RootModel
from typing import Dict, List

class BookTagM2MCreate(BaseModel):
    book_id: int
    tag_id: int

class BookTagM2MResponse(BaseModel):
    id: int
    book_id: int
    tag_id: int

class BookTagM2MUpdate(BaseModel):
    book_id: int = None
    tag_id: int = None

class BookTagGroupResponse(RootModel[Dict[int, List[int]]]):
    pass