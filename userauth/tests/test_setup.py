from rest_framework.test import APITestCase
from django.urls import reverse

class TestSetUp(APITestCase):

    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')

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