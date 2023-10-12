from .test_setup import TestSetUp
from django.urls import reverse

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


    def test_get_all_completed_filtered_notes_authenticated_user(self):

        # Provide authorization credentials --> option 2
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Get item from --self.notes_url-- route in the parent class
        res = self.client.get(self.get_filtered_notes_url)
        
        # Assert res.status_code == 200
        self.assertEqual(res.status_code, 200)


    def test_get_all_createdAt_ordered_notes_authenticated_user(self):
    
        # Provide authorization credentials --> option 2
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Get item from --self.notes_url-- route in the parent class
        res = self.client.get(self.get_ordered_notes_url)
        
        # Assert res.status_code == 200
        self.assertEqual(res.status_code, 200)


    def test_get_all_priority_ordered_notes_authenticated_user(self):
        
        # Provide authorization credentials --> option 2
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Get item from --self.notes_url-- route in the parent class
        res = self.client.get(self.get_ordered_notes_by_priority_url)
        
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
        response = self.client.post(self.create_notes_url, self.note_data)
        new_note_id = response.data['id'] 

        notes_detail_url = reverse('notes_detail', kwargs={'note_id': new_note_id})

        # Get item by id
        res = self.client.get(notes_detail_url)

        # assert res.status_code equal 200
        self.assertEqual(res.status_code, 200)

    def test_cannot_update_item_if_not_found(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Update note title to Updated Title
        self.note_data['title'] = "Updated Title"

        # Update on item that does not exist
        res = self.client.patch(self.notes_detail_url, self.note_data)

        # assert res.status_code equal 400
        self.assertEqual(res.status_code, 400)


    def test_can_update_item(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create a new item 
        response = self.client.post(self.create_notes_url, self.note_data)
        new_note_id = response.data['id'] 

        notes_detail_url = reverse('notes_detail', kwargs={'note_id': new_note_id})
        
        # Update note title to Updated Title
        self.note_data['title'] = "Updated Title"

        # Update it with new data of --self.update_note_data--
        res = self.client.patch(notes_detail_url, self.note_data)

        # import pdb
        # pdb.set_trace()

        # Assert the new data is not equal to the old data
        self.assertNotEqual(res.data, self.note_data)

        # assert updated date title is Updated Title from Hey of the origin data
        self.assertEqual(res.data['title'], "Updated Title")

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
        response = self.client.post(self.create_notes_url, self.note_data)
        new_note_id = response.data['id'] 

        notes_detail_url = reverse('notes_detail', kwargs={'note_id': new_note_id})

        # Delete created item
        res = self.client.delete(notes_detail_url)

        # assert res.status_code equal 200
        self.assertEqual(res.status_code, 200)

class TestFileGeneratingViews(TestSetUp):

    def test_can_generate_pdf_view(self):
        #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create new item
        res = self.client.get(self.generate_pdf_url)

        # assert res.status_code equal 200
        self.assertEqual(res.status_code, 200)


    def test_can_generate_csv_view(self):
            #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create new item
        res = self.client.get(self.generate_csv_url)

        # assert res.status_code equal 200
        self.assertEqual(res.status_code, 200)


    def test_can_generate_excel_view(self):
            #provide authorization credentials
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Create new item
        res = self.client.get(self.generate_excel_url)

        # assert res.status_code equal 200
        self.assertEqual(res.status_code, 200)