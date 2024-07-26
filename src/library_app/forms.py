from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

User = get_user_model()


class LibrarianSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "tab_number")


class ReaderSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "password1", "password2", "first_name", "last_name", "address")


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ("username", "password")
