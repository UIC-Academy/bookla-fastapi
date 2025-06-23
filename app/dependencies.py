from fastapi import Depends, Query
from sqlalchemy.orm import Session

from typing import Annotated

from app.database import SessionLocal


async def pagination_dependency(limit: int = Query(10, ge=1, le=100), offset: int = Query(0, ge=0)):
    return {"limit": limit, "offset": offset}


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

pagination_dep = Annotated[dict, Depends(pagination_dependency)]
db_dep = Annotated[Session, Depends(get_db)]
