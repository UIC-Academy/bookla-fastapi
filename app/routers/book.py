from fastapi import APIRouter, HTTPException, Response
from app.dependencies import db_dep, pagination_dep
from app.models import Author, Book, Category, Publisher
from app.schemas import BookCreate, BookListResponse, BookUpdate, BookDictResponse

router = APIRouter(
    prefix="/book",
    tags=["book"]
)

@router.get("/list/", response_model=list[BookListResponse], status_code=200)
async def list_books(db: db_dep):
    books = db.query(Book).all()
    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    return books

@router.get("/{id}", response_model=BookListResponse, status_code=200)
async def get_book(id: int, db: db_dep):
    book = db.query(Book).filter(Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.get("/search/book name/", response_model=BookDictResponse, status_code=200)
async def search_books(name: str, db: db_dep, limit: int = 10, offset: int = 0):
    query = db.query(Book).filter(Book.name.ilike(f"%{name}%"))
    total_count = query.count()
    books = query.offset(offset).limit(limit).all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")
    
    return {
        "total_count": total_count,
        "books": books
    }

@router.get("/search/author/{author_name}", response_model=BookDictResponse, status_code=200)
async def search_books_by_author(author_name: str, db: db_dep, limit: int = 10, offset: int = 0):
    query = db.query(Book).join(Author).filter(Author.fullname.ilike(f"%{author_name}%"))
    total_count = query.count()
    books = query.offset(offset).limit(limit).all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")

    return {
        "total_count": total_count,
        "books": books
    }

@router.get("/search/category/{category_name}", response_model=BookDictResponse, status_code=200)
async def search_books_by_category(category_name: str, db: db_dep, limit: int = 10, offset: int = 0):
    query = db.query(Book).join(Category).filter(Category.name.ilike(f"%{category_name}%"))
    total_count = query.count()
    books = query.offset(offset).limit(limit).all()

    if not books:
        raise HTTPException(status_code=404, detail="No books found")

    return {
        "total_count": total_count,
        "books": books
    }

@router.post("/create/", response_model=BookListResponse, status_code=201)
async def create_book(book: BookCreate, db: db_dep):

    existing_book = db.query(Book).filter(Book.isbn == book.isbn).first()
    if existing_book:
        raise HTTPException(status_code=409, detail="Bu ISBN allaqachon mavjud.")


    new_book = Book(**book.model_dump())
    author = db.query(Author).filter(Author.id == book.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    category = db.query(Category).filter(Category.id == book.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    publisher = db.query(Publisher).filter(Publisher.id == book.publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@router.put("/update/{id}", response_model=BookListResponse, status_code=200)
async def update_book(id: int, book: BookUpdate, db: db_dep):
    book_obj = db.query(Book).filter(Book.id == id).first()
    if not book_obj:
        raise HTTPException(status_code=404, detail="Book not found")
    author = db.query(Author).filter(Author.id == book.author_id).first()
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")

    category = db.query(Category).filter(Category.id == book.category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    publisher = db.query(Publisher).filter(Publisher.id == book.publisher_id).first()
    if not publisher:
        raise HTTPException(status_code=404, detail="Publisher not found")

    for key, value in book.model_dump(exclude_unset=True).items():
        setattr(book_obj, key, value)
    
    db.commit()
    db.refresh(book_obj)
    return book_obj

@router.patch("/update/{id}", response_model=BookUpdate, status_code=200)
async def update_book_partial(id: int, book: BookUpdate, db: db_dep):
    book_obj = db.query(Book).filter(Book.id == id).first()
    if not book_obj:
        raise HTTPException(status_code=404, detail="Book not found")

    update_data = book.model_dump(exclude_unset=True)

    if 'author_id' in update_data:
        author = db.query(Author).filter(Author.id == update_data['author_id']).first()
        if not author:
            raise HTTPException(status_code=404, detail="Author not found")

    if 'category_id' in update_data:
        category = db.query(Category).filter(Category.id == update_data['category_id']).first()
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

    if 'publisher_id' in update_data:
        publisher = db.query(Publisher).filter(Publisher.id == update_data['publisher_id']).first()
        if not publisher:
            raise HTTPException(status_code=404, detail="Publisher not found")

    # endi update qilamiz
    for key, value in update_data.items():
        setattr(book_obj, key, value)

    
    db.commit()
    db.refresh(book_obj)
    return book_obj

@router.delete("/delete/{id}", status_code=204)
async def delete_book(id: int, db: db_dep):
    book = db.query(Book).filter(Book.id == id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return Response(status_code=204)

