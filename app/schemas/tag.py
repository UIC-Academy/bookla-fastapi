from pydantic import BaseModel

class TagCreate(BaseModel):
    name: str

class TagListResponse(BaseModel):
    id: int
    name: str
