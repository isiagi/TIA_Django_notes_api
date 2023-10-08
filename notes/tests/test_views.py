from .test_setup import TestSetUp

class TestViews(TestSetUp):
    def test_get_all_notes_for_authenticated_user(self):

        # force login --> option 1
        # self.client.force_login(user=self.user)

        # Provide authorization credentials --> option 2
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Get item from --self.notes_url-- route in the parent class
        res = self.client.get(self.get_notes_url)
        
        # Assert res.status_code == 200
        self.assertEqual(res.status_code, 200)


    def test_user_can_create_note(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # create a an item
        res = self.client.post(self.create_notes_url, self.note_data)

        # assert res.status_code equal 201
        self.assertEqual(res.status_code, 201)


class TestViewsDetail(TestSetUp):
    def test_cannot_get_item_by_id_if_not_found(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Get note by id using route in --self.notes_detail_url--
        res = self.client.get(self.notes_detail_url)

        # assert res.status_code equal 400
        self.assertEqual(res.status_code, 400)


    def test_get_item_by_id_if_found(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create new item to be fetched
        self.client.post(self.create_notes_url, self.note_data)

        # Get item by id
        res = self.client.get(self.notes_detail_url)

        # assert res.status_code equal 200
        self.assertEqual(res.status_code, 200)

    def test_cannot_update_item_if_not_found(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Update on item that does not exist
        res = self.client.patch(self.notes_detail_url, self.update_note_data)

        # assert res.status_code equal 400
        self.assertEqual(res.status_code, 400)


    def test_can_update_item(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create a new item 
        self.client.post(self.create_notes_url, self.note_data)

        # Update it with new data of --self.update_note_data--
        res = self.client.patch(self.notes_detail_url, self.update_note_data)

        # Assert the new data is not equal to the old data
        self.assertNotEqual(res.data, self.note_data)

        # assert res.status_code equal 201
        self.assertEqual(res.status_code, 201)


    def test_cannot_delete_item_by_id_if_not_found(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Delete item that doesnot exist
        res = self.client.delete(self.notes_detail_url)

        # assert res.status_code equal 400
        self.assertEqual(res.status_code, 400)


    def test_can_delete_item_by_id(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create new item
        self.client.post(self.create_notes_url, self.note_data)

        # Delete created item
        res = self.client.delete(self.notes_detail_url)

        # assert res.status_code equal 200
        self.assertEqual(res.status_code, 200)