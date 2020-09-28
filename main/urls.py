from django.urls import path

from . import views

urlpatterns = [
path("<str:name>", views.index, name="index"),
path("new/", views.v1, name = "new view"),
]