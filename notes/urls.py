from django.urls import path
from .views import NotesCreateApiView, NotesDetailApiView, GetNotesApiView, NotesPdfApiView, PublishPdfApiView, CSVExportView, ExcelExportView

urlpatterns = [
    path('', GetNotesApiView.as_view(), name="get_notes"),
    path('create', NotesCreateApiView.as_view(), name="create_notes"),
    path('<int:note_id>', NotesDetailApiView.as_view(), name="notes_detail"),
    path('generate_pdf', NotesPdfApiView.as_view(), name="generate_pdf"),
    path('publish_pdf', PublishPdfApiView.as_view(), name="publish_pdf"),
    path('generate_csv', CSVExportView.as_view(), name="generate_csv"),
    path('generate_excel', ExcelExportView.as_view(), name="generate_excel"),
]
