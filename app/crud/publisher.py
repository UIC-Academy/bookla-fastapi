from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models import Publisher
from app.schemas import PublisherCreate

async def create_publisher(db: AsyncSession, schema: PublisherCreate):
    publisher = Publisher(**schema.dict())
    db.add(publisher)
    await db.commit()
    await db.refresh(publisher)
    return publisher

async def get_all_publishers(db: AsyncSession):
    result = await db.execute(select(Publisher))
    return result.scalars().all()

async def get_publisher_by_id(db: AsyncSession, publisher_id: int):
    result = await db.execute(select(Publisher).where(Publisher.id == publisher_id))
    return result.scalar_one_or_none()
