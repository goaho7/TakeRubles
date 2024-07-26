from rest_framework import serializers

from library_app.models import Book, BorrowRecord


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowRecord
        fields = "__all__"
