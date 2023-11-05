from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    path("", include("clauding_app.urls")),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)