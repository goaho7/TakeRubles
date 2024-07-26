from django.urls import path

from api import views

urlpatterns = [
    path("books/", views.BookListView.as_view(), name="api_book_list"),
    path("books/borrow/<int:book_id>/", views.BorrowBookView.as_view(), name="api_borrow_book"),
    path("books/return/<int:book_id>/", views.ReturnBookView.as_view(), name="api_return_book"),
    path("my_books/", views.MyBooksView.as_view(), name="api_my_books"),
]
