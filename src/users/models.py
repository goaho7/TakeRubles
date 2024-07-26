from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    LIBRARIAN = "librarian"
    READER = "reader"

    ROLES = (
        (LIBRARIAN, "Библиотекарь"),
        (READER, "Читатель"),
    )
    role = models.CharField(verbose_name="Роль", default="reader", choices=ROLES, max_length=15)
    tab_number = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    address = models.TextField(null=True, blank=True)
