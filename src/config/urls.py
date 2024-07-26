from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("users.urls")),
    path("auth/", include("django.contrib.auth.urls")),
    path("", include("library_app.urls")),
    path("api/", include("api.urls")),
    path("users/", include("users.urls")),
]