from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey

from typing import Optional
from datetime import datetime, timezone

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100), unique=True)

    is_active: Mapped[bool] = mapped_column(default=True)
    is_deleted: Mapped[bool] = mapped_column(default=False)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc)
    )

    user_books: Mapped[list["Book"]] = relationship(
        secondary="UserBook", back_populates="users"
    )
    comments: Mapped[list["Book"]] = relationship(
        secondary="Comment", back_populates="comment_owners"
    )

    def __str__(self):
        return f"User(id={self.id}, email={self.email})"


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(String(1000), nullable=True)
    isbn: Mapped[str] = mapped_column(String(100), unique=True)
    cover: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    page_count: Mapped[int]
    author_id: Mapped[int] = mapped_column(Integer, ForeignKey("authors.id"))
    category_id: Mapped[int] = mapped_column(Integer, ForeignKey("categories.id"))
    publisher_id: Mapped[int] = mapped_column(Integer, ForeignKey("publishers.id"))
    rating: Mapped[float] = mapped_column(default=0.0)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc)
    )

    author: Mapped["Author"] = relationship(back_populates="books")
    category: Mapped["Category"] = relationship(back_populates="books")
    publisher: Mapped["Publisher"] = relationship(back_populates="books")
    tags: Mapped[list["Tag"]] = relationship(
        secondary="book_tag_m2m", back_populates="books"
    )
    users: Mapped[list["User"]] = relationship(
        secondary="UserBook", back_populates="user_books"
    )
    comment_owners: Mapped[list["User"]] = relationship(
        secondary="Comment", back_populates="comments"
    )

    def __str__(self):
        return f"Book(id={self.id}, name={self.name})"


class UserBook(Base):
    __tablename__ = "user_books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.id"))
    current_page: Mapped[int] = mapped_column(default=0)
    started_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    finished_at: Mapped[datetime] = mapped_column(nullable=True, default=None)

    def __str__(self):
        return f"UserBook(id={self.id}, user_id={self.user_id}, book_id={self.book_id})"


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id"))
    book_id: Mapped[int] = mapped_column(Integer, ForeignKey("books.id"))
    text: Mapped[str] = mapped_column(String(1000))
    reply_to: Mapped[int] = mapped_column(ForeignKey("comments.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))

    def __str__(self):
        return f"Comment(id={self.id}, user_id={self.user_id}, book_id={self.book_id})"


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    fullname: Mapped[str] = mapped_column(String(100))
    bio: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    avatar: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc)
    )

    books: Mapped["Book"] = relationship(back_populates="author")

    def __str__(self):
        return f"Author(id={self.id}, fullname={self.fullname})"


class Publisher(Base):
    __tablename__ = "publishers"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    location_url: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    website_url: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc)
    )

    books: Mapped["Book"] = relationship(back_populates="publisher")

    def __str__(self):
        return f"Publisher(id={self.id}, name={self.name})"


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    books: Mapped["Book"] = relationship(back_populates="category")

    def __str__(self):
        return f"Category(id={self.id}, name={self.name})"


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100))

    books: Mapped[list["Book"]] = relationship(
        secondary="book_tag_m2m", back_populates="tags"
    )

    def __str__(self):
        return f"Tag(id={self.id}, name={self.name})"


class BookTagM2M(Base):
    __tablename__ = "book_tag_m2m"

    book_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("books.id"), primary_key=True
    )
    tag_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("tags.id"), primary_key=True
    )

    def __str__(self):
        return f"BookTagM2M(book_id={self.book_id}, tag_id={self.tag_id})"
