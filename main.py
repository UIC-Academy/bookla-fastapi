from fastapi import FastAPI

from app.routers.category import router as category_router

app = FastAPI(
    title = "Bookla",
    description = "Bookla - is a FastAPI application, built for practicing CRUD and authentication mechanisms in FastAPI",
    version = "0.0.1"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(category_router)