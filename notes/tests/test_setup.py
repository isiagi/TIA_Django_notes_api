from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TestSetUp(APITestCase):

    def setUp(self):
        self.notes_url = reverse('notes')
        self.notes_detail_url = reverse('notes_detail', kwargs={'note_id': 1})
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')
        self.token = Token.objects.create(user=self.user)

        self.note_data = {
            "title": "hey",
            "description": "hello",
            "due_date": "2033-09-20",
            "user": self.user.id
        }

        self.update_note_data = {
            "title": "update",
            "description": "hello",
            "due_date": "2033-09-20",
            "user": self.user.id
        }

        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    
