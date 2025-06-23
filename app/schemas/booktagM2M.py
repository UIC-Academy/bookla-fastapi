from pydantic import BaseModel

class BookTagM2MResponse(BaseModel):
    book_id: int
    tag_id: int
