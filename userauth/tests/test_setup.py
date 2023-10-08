from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')

        self.user_data = {
            "email": "try@mail5.com",
             "password": "geofrey124",
             "first_name": "try",
            "last_name": "man",
            "username": "jeff5"
            }

        return super().setUp()


    def tearDown(self):
        return super().tearDown()