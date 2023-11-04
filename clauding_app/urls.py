from django.urls import path

from . import views

urlpatterns = [
    #path("<str:question_id>/", views.get_markdown, name="get_markdown"),
    path("", views.index, name="index"),
    path("submit/", views.submit, name="submit"),
]