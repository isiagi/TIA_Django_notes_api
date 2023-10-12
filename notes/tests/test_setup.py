from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TestSetUp(APITestCase):

    def setUp(self):
        self.get_notes_url = reverse('get_notes')
        self.get_filtered_notes_url = f"{reverse('get_notes')}?completed=True"
        self.get_ordered_notes_url = f"{reverse('get_notes')}?ordering=created_at"
        self.get_ordered_notes_by_priority_url = f"{reverse('get_notes')}?ordering=priority"
        self.create_notes_url = reverse('create_notes')
        self.generate_pdf_url = reverse('generate_pdf')
        self.generate_csv_url = reverse('generate_csv')
        self.generate_excel_url = reverse('generate_excel')
        self.notes_detail_url = reverse('notes_detail', kwargs={'note_id': 1})
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)

        self.note_data = {
            "title": "hey",
            "description": "hello",
            "due_date": "2033-09-20",
            "category": "Personal",
            "user": self.user.id
        }

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
