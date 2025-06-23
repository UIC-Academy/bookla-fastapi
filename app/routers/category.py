from fastapi import APIRouter, HTTPException, Response

from app.dependencies import db_dep, pagination_dep
from app.models import Category
from app.schemas import CategoryCreate, CategoryListResponse


router = APIRouter(
    tags=["category"]
)


@router.get("/categories/", response_model=list[CategoryListResponse], status_code=200)
async def list_category(db: db_dep):
    categories = db.query(Category).all()
    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")
    
    return categories


@router.get("/category/{category_id}", response_model=CategoryListResponse, status_code=200)
async def get_category(category_id: int, db: db_dep):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category


@router.post("/category/create/", response_model=CategoryListResponse, status_code=201)
async def create_category(category: CategoryCreate, db: db_dep):
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.put("/category/{id}/update/", response_model=CategoryListResponse, status_code=200)
async def update_category(id: int, category: CategoryCreate, db: db_dep):
    category_obj = db.query(Category).filter(Category.id == id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category_obj.name = category.name
    db.commit()
    db.refresh(category_obj)
    return category_obj

@router.patch("/category/{category_id}/update/", response_model=CategoryListResponse, status_code=200)
async def update_category(category_id: int, category: CategoryCreate, db: db_dep):
    category_obj = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category_obj.name = category.name if category.name else category_obj.name
    db.commit()
    db.refresh(category_obj)
    return category_obj

@router.delete("/category/{category_id}/delete/", status_code=204)
async def delete_category(category_id: int, db: db_dep):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(category)
    db.commit()