from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class BorrowRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="borrow_record")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="borrow_record")
    borrowed_at = models.DateTimeField(auto_now_add=True)
    returned_at = models.DateTimeField(null=True, blank=True)

    def days_borrowed(self):
        if self.returned_at:
            return (self.returned_at - self.borrowed_at).days
        return (timezone.now() - self.borrowed_at).days
