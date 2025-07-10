from typing import ClassVar

from starlette_admin.contrib.sqla import ModelView


class UserAdminView(ModelView):
    fields: ClassVar[list[str]] = [
        "id",
        "email",
        "username",
        "is_active",
        "is_admin",
        "is_deleted",
        "created_at",
    ]
    exclude_fields_from_list: ClassVar[list[str]] = ["created_at"]
    exclude_fields_from_create: ClassVar[list[str]] = ["created_at"]
    exclude_fields_from_edit: ClassVar[list[str]] = ["created_at"]
    export_fields: ClassVar[list[str]] = [
        "id",
        "email",
        "username",
        "is_active",
        "created_at",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]


class BookAdminView(ModelView):
    fields: ClassVar[list[str]] = [
        "id",
        "name",
        "description",
        "isbn",
        "tags",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_list: ClassVar[list[str]] = ["created_at", "updated_at"]
    exclude_fields_from_create: ClassVar[list[str]] = ["created_at", "updated_at"]
    exclude_fields_from_edit: ClassVar[list[str]] = ["created_at", "updated_at"]
    export_fields: ClassVar[list[str]] = [
        "id",
        "name",
        "description",
        "isbn",
        "tags",
        "created_at",
        "updated_at",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]
