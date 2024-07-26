from django.contrib.auth import get_user_model
from rest_framework import serializers

from library_app.models import Book, BorrowRecord

User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ("title", "author", "genre")


class BorrowSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="book.title", read_only=True)

    class Meta:
        model = BorrowRecord
        fields = ("title", "borrowed_at", "days_borrowed")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
