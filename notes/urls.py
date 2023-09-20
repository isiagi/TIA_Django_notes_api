from django.urls import path
from .views import NotesListApiView, NotesDetailApiView

urlpatterns = [
    path('', NotesListApiView.as_view()),
    path('<int:note_id>', NotesDetailApiView.as_view())
]
