from fastapi import FastAPI

from app.routers import category, author, publisher, tag, book 

app = FastAPI(
    title = "Bookla",
    description = "Bookla - is a FastAPI application, built for practicing CRUD and authentication mechanisms in FastAPI",
    version = "0.0.1"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(category.router)
app.include_router(author.router)
app.include_router(publisher.router)
app.include_router(tag.router)
app.include_router(book.router)