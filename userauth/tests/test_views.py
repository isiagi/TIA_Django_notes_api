from .test_setup import TestSetUp
from rest_framework.authtoken.models import Token

class TestViews(TestSetUp):
    def test_user_cannot_register_without_user_data_view(self):
        res = self.client.post(self.register_url)
        # import pdb
        # pdb.set_trace()
        self.assertEqual(res.status_code, 400)



    def test_user_can_register_view(self):
        res = self.client.post(self.register_url, self.user_data, format="json",)
        # import pdb
        # pdb.set_trace()
        self.assertNotEqual(res.data['Token'], "")
        self.assertEqual(res.status_code, 201)

    def test_user_cannot_login_minus_registering_view(self):
        res = self.client.post(self.login_url, self.user_data, format="json")
        
        self.assertEqual(res.status_code, 404)


    def test_user_can_login_view(self):
        self.client.post(self.register_url, self.user_data, format="json",)

        res = self.client.post(self.login_url, self.user_data, format="json")
        
        self.assertEqual(res.status_code, 200)


    def test_user_cannot_login_with_wrong_password_view(self):
        self.client.post(self.register_url, self.user_data, format="json",)

        self.user_data['password'] = "wrongpassword"
        res = self.client.post(self.login_url, self.user_data, format="json")
        
        self.assertEqual(res.data['message'], "Invalid Username or Password")
        self.assertEqual(res.status_code, 400)


    def test_user_cannot_logout_if_not_login_view(self):
        res = self.client.get(self.logout_url)

        self.assertEqual(res.status_code, 403)


    def test_user_cannot_logout_if_not_having_token_view(self):
        res = self.client.get(self.logout_url)

        self.assertEqual(res.status_code, 403)


    def test_user_can_logout_view(self):
        # force login --> option 1
        self.client.force_login(user=self.user)
        
        Token.objects.create(user=self.user)
        
        res = self.client.get(self.logout_url)
        
        self.assertEqual(res.status_code, 200)