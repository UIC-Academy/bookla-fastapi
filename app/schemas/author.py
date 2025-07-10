from pydantic import BaseModel


class AuthorCreate(BaseModel):
    fullname: str
    bio: str | None = None
    avatar: str | None = None


class AuthorListResponse(BaseModel):
    id: int
    fullname: str
    bio: str | None = None
    avatar: str | None = None
