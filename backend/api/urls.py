from django.urls import path
from . import views

urlpatterns = [
    path("notes/",views.NoteListCreate.as_view(), name = "note-list"),
    #pk stands for primary key
    path("notes/delete/<int:pk>/", views.NoteDelete.as_view(), name = "delete-notes"),
]
