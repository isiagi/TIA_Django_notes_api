from django.urls import path
from .views import NotesCreateApiView, NotesDetailApiView, GetNotesApiView

urlpatterns = [
    path('', GetNotesApiView.as_view(), name="get_notes"),
    path('create', NotesCreateApiView.as_view(), name="create_notes"),
    path('<int:note_id>', NotesDetailApiView.as_view(), name="notes_detail"),
]
