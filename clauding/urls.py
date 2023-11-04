from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("clauding_app.urls")),
    path("admin/", admin.site.urls),
]