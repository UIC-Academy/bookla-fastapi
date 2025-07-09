from fastapi import Depends
from sqlalchemy.orm import Session

from typing import Annotated

from app.database import SessionLocal


async def pagination_depedency(q: str | None = None, offset: int = 0, limit: int = 100):
    return {"q": q, "offset": offset, "limit": limit}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


pagination_dep = Annotated[dict, Depends(pagination_depedency)]
db_dep = Annotated[Session, Depends(get_db)]
