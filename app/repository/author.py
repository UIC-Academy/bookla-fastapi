from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.author import Author
from app.schemas.author import AuthorCreate
from typing import List


async def create_author(session: AsyncSession, author_create: AuthorCreate) -> Author:
    new_author = Author(name=author_create.name)
    session.add(new_author)
    await session.commit()
    await session.refresh(new_author)
    return new_author


async def get_all_authors(session: AsyncSession) -> List[Author]:
    query = select(Author)
    result = await session.execute(query)
    return result.scalars().all()


async def get_author(session: AsyncSession, author_id: int) -> Author | None:
    return await session.get(Author, author_id)


async def delete_author(session: AsyncSession, author_id: int) -> None:
    author = await session.get(Author, author_id)
    if author:
        await session.delete(author)
        await session.commit()
