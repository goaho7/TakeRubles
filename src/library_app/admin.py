from django.contrib import admin

from library_app.models import Book, BorrowRecord


@admin.register(Book)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "genre")


@admin.register(BorrowRecord)
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "book", "borrowed_at", "returned_at")
