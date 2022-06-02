from django.test import TestCase


class TestMain(TestCase):
    """Tests class"""

    def test_index_page_get_request(self):
        """Get request index test"""
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_index_page_post_request_correct_date(self):
        """Get request index test"""
        response = self.client.post('', data={'date': '2021-10-15'})
        self.assertContains(response, "Week number is 146")

    def test_index_page_post_request_incorrect_date(self):
        """Get request index test"""
        response = self.client.post('', data={'date': '2021-10-55'})
        self.assertContains(response, "Enter a valid date")

    def test_index_page_post_request_past_date(self):
        """Get request index test"""
        response = self.client.post('', data={'date': '2018-10-55'})
        self.assertNotContains(response, "Week number is")
