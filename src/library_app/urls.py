from django.urls import path

from . import views

app_name = "library_app"


urlpatterns = [
    path("", views.index, name="index"),
    path("my_books/", views.my_books, name="my_books"),
    path("borrow/<int:book_id>/", views.borrow_book, name="borrow_book"),
    path("return/<int:book_id>/", views.return_book, name="return_book"),
]
