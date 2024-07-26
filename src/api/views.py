from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookSerializer, BorrowSerializer
from library_app.models import Book, BorrowRecord


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BorrowBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        if not book.is_borrowed:
            BorrowRecord.objects.create(user=request.user, book=book)
            book.is_borrowed = True
            book.save()
        return Response({"status": "book borrowed"})


class ReturnBookView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, book_id):
        book = Book.objects.get(id=book_id)
        borrow_record = BorrowRecord.objects.filter(user=request.user, book=book, returned=False).first()
        if borrow_record:
            borrow_record.returned = True
            borrow_record.save()
            book.is_borrowed = False
            book.save()
        return Response({"status": "book returned"})


class MyBooksView(generics.ListAPIView):
    serializer_class = BorrowSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BorrowRecord.objects.filter(user=self.request.user, returned=False)
