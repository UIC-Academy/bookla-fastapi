from fastapi import FastAPI

from app.admin.settings import admin
from app.routers.auth import router as auth_router
from app.routers.author import router as author_router
from app.routers.book import router as book_router
from app.routers.category import router as category_router
from app.routers.publisher import router as publisher_router
from app.routers.tag import router as tag_router
from app.routers.user import router as users_router

app = FastAPI(
    title="Bookla",
    description="Bookla - is a FastAPI application, built for practicing CRUD and authentication mechanisms in FastAPI",
    version="0.0.1",
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(category_router)
app.include_router(author_router)
app.include_router(publisher_router)
app.include_router(tag_router)
app.include_router(book_router)
app.include_router(auth_router)
app.include_router(users_router)

admin.mount_to(app=app)
