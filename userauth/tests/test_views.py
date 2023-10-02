from .test_setup import TestSetUp

class TestViews(TestSetUp):
    def test_user_cannot_register_view(self):
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