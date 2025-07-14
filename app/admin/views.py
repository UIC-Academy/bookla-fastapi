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
        "cover",
        "rating",
        "is_active",
        "created_at",
    ]
    exclude_fields_from_list: ClassVar[list[str]] = [
        "cover",
        "created_at",
        "updated_at",
    ]
    exclude_fields_from_create: ClassVar[list[str]] = ["created_at", "updated_at"]
    exclude_fields_from_edit: ClassVar[list[str]] = ["created_at", "updated_at"]
    export_fields: ClassVar[list[str]] = [
        "id",
        "name",
        "description",
        "isbn",
        "rating",
        "is_active",
        "created_at",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]


class UserBookAdminView(ModelView):
    fields: ClassVar[list[str]] = [
        "id",
        "user",
        "book",
        "started_at",
    ]
    exclude_fields_from_list: ClassVar[list[str]] = ["started_at"]
    exclude_fields_from_create: ClassVar[list[str]] = ["started_at"]
    exclude_fields_from_edit: ClassVar[list[str]] = ["started_at"]
    export_fields: ClassVar[list[str]] = [
        "id",
        "user_id",
        "book_id",
        "started_at",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]


class CommentAdminView(ModelView):
    fields: ClassVar[list[str]] = [
        "id",
        "user",
        "book",
        "text",
        "created_at",
    ]
    exclude_fields_from_list: ClassVar[list[str]] = ["created_at"]
    exclude_fields_from_create: ClassVar[list[str]] = ["created_at"]
    exclude_fields_from_edit: ClassVar[list[str]] = ["created_at"]
    export_fields: ClassVar[list[str]] = [
        "id",
        "user_id",
        "book_id",
        "text",
        "reply_to",
        "created_at",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]


class AuthorAdminView(ModelView):
    fields: ClassVar[list[str]] = [
        "id",
        "fullname",
        "bio",
        "avatar",
        "created_at",
    ]
    exclude_fields_from_list: ClassVar[list[str]] = ["created_at"]
    exclude_fields_from_create: ClassVar[list[str]] = ["created_at"]
    exclude_fields_from_edit: ClassVar[list[str]] = ["created_at"]
    export_fields: ClassVar[list[str]] = [
        "id",
        "fullname",
        "bio",
        "avatar",
        "created_at",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]


class PublisherAdminView(ModelView):
    fields: ClassVar[list[str]] = [
        "id",
        "name",
        "location_url",
        "website_url",
        "created_at",
    ]
    exclude_fields_from_list: ClassVar[list[str]] = ["created_at"]
    exclude_fields_from_create: ClassVar[list[str]] = ["created_at"]
    exclude_fields_from_edit: ClassVar[list[str]] = ["created_at"]
    export_fields: ClassVar[list[str]] = [
        "id",
        "name",
        "location_url",
        "website_url",
        "created_at",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]


class CategoryAdminView(ModelView):
    fields: ClassVar[list[str]] = [
        "id",
        "name",
    ]
    export_fields: ClassVar[list[str]] = [
        "id",
        "name",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]


class TagAdminView(ModelView):
    fields: ClassVar[list[str]] = [
        "id",
        "name",
    ]
    export_fields: ClassVar[list[str]] = [
        "id",
        "name",
    ]
    export_types: ClassVar[list[str]] = ["csv", "excel", "pdf", "print"]
