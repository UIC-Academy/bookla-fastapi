from pydantic import BaseModel


class CategoryCreate(BaseModel):
    name: str


class CategoryListResponse(BaseModel):
    id: int
    name: str