from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("read/", view=views.read_file_content, name="read"),
    path("download/", view=views.save_in_server, name="download"),
    path("save/", view=views.save_in_server, name="save"),
    path("readDb", view=views.readDb, name="readDb")
]