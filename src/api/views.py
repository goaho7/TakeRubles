from django.utils import timezone
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers import BookSerializer, BorrowSerializer
from library_app.models import Book, BorrowRecord


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["post"])
    def borrow(self, request, pk=None):
        book = self.get_object()
        if not BorrowRecord.objects.filter(book=book, user=request.user, returned_at__isnull=True).exists():
            BorrowRecord.objects.create(book=book, user=request.user)
        return Response({"status": "book borrowed"})

    @action(detail=True, methods=["post"])
    def return_book(self, request, pk=None):
        book = self.get_object()
        borrow_record = BorrowRecord.objects.filter(book=book, user=request.user, returned_at__isnull=True).first()
        if borrow_record:
            borrow_record.returned_at = timezone.now()
            borrow_record.save()
            return Response({"status": "book returned"})
        else:
            return Response({"status": "you did not borrow this book"}, status=status.HTTP_400_BAD_REQUEST)


class BorrowedBooksView(APIView):
    """Список книг на руках"""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        my_books = request.user.borrow_record.all()
        serializer = BorrowSerializer(my_books, many=True)
        return Response(serializer.data)
