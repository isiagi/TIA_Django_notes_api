from django.urls import path
from .views import NotesListApiView, NotesDetailApiView

urlpatterns = [
    path('', NotesListApiView.as_view(), name="notes"),
    path('<int:note_id>', NotesDetailApiView.as_view(), name="notes_detail")
]
