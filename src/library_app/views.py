from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Book, BorrowRecord
from .utils import paginat

User = get_user_model()


def index(request):
    books = Book.objects.all()
    debtors = BorrowRecord.objects.select_related("user", "book")
    borrow_books = []
    if request.user.is_authenticated:
        borrows = request.user.borrow_record.all()
        for borrow in borrows:
            if not borrow.returned_at:
                borrow_books.append(borrow.book.id)
        page_obj = paginat(request, books)
        context = {"page_obj": page_obj, "borrow_books": borrow_books, "debtors": debtors}
        return render(request, "library/index.html", context)
    return redirect("users:login")


@login_required
def borrow_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if not BorrowRecord.objects.filter(book=book, user=request.user, returned_at__isnull=True).exists():
        BorrowRecord.objects.create(book=book, user=request.user)
    return redirect("library_app:index")


@login_required
def return_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    borrow_record = BorrowRecord.objects.filter(book=book, user=request.user, returned_at__isnull=True).first()
    if borrow_record:
        borrow_record.returned_at = timezone.now()
        borrow_record.save()
    return redirect("library_app:index")


@login_required
def my_books(request):
    borrows = request.user.borrow_record.filter(returned_at__isnull=True).order_by("book__title")
    return render(request, "library/my_books.html", {"borrows": borrows})
