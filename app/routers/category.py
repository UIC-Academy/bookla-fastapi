from fastapi import APIRouter, HTTPException, Response

from app.dependencies import db_dep
from app.models import Category
from app.schemas import CategoryCreate, CategoryListResponse


router = APIRouter(
    prefix="/category",
    tags=["category"]
)


@router.get("/", response_model=list[CategoryListResponse])
async def list_category(db: db_dep):
    categories = db.query(Category).all()
    if not categories:
        raise HTTPException(status_code=404, detail="No categories found")
    
    return categories


@router.get("/{category_id}", response_model=CategoryListResponse)
async def get_category(category_id: int, db: db_dep):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    return category


@router.post("/create/", response_model=CategoryListResponse)
async def create_category(category: CategoryCreate, db: db_dep):
    new_category = Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.put("/{category_id}/update/", response_model=CategoryListResponse)
async def update_category(category_id: int, category: CategoryCreate, db: db_dep):
    category_obj = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    category_obj.name = category.name
    db.commit()
    db.refresh(category_obj)
    return category_obj


@router.delete("/{category_id}/delete/")
async def delete_category(category_id: int, db: db_dep):
    category = db.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    db.delete(category)
    db.commit()
    return Response(status_code=204)