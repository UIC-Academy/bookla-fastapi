from fastapi import APIRouter
from app.routers import tag

router = APIRouter()
router.include_router(tag.router)
from .publisher import router as publisher_router
