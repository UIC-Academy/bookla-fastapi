from starlette_admin.contrib.sqla import Admin

from app.admin.views import (
    AuthorAdminView,
    BookAdminView,
    CategoryAdminView,
    CommentAdminView,
    PublisherAdminView,
    TagAdminView,
    UserAdminView,
    UserBookAdminView,
)
from app.database import engine
from app.models import Author, Book, Category, Comment, Publisher, Tag, User, UserBook

admin = Admin(
    engine=engine,
    title="Bookla Admin",
    base_url="/admin",
)

admin.add_view(UserAdminView(User, icon="fa fa-user"))
admin.add_view(BookAdminView(Book, icon="fa fa-book"))
admin.add_view(UserBookAdminView(UserBook, icon="fa fa-user"))
admin.add_view(AuthorAdminView(Author, icon="fa fa-user"))
admin.add_view(PublisherAdminView(Publisher, icon="fa fa-school"))
admin.add_view(CategoryAdminView(Category, icon="fa fa-folder"))
admin.add_view(CommentAdminView(Comment, icon="fa fa-comment"))
admin.add_view(TagAdminView(Tag, icon="fa fa-tag"))
