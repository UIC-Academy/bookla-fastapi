from starlette_admin.contrib.sqla import Admin

from app.admin.views import UserAdminView
from app.database import engine
from app.models import User

admin = Admin(
    engine=engine,
    title="Bookla Admin",
    base_url="/admin",
)

admin.add_view(UserAdminView(User, icon="fa fa-user"))
