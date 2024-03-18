from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("read/", view=views.read_file_content, name="read")
]