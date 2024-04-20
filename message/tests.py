from django.test import SimpleTestCase

# Create your tests here.
class testPage(SimpleTestCase):
    def test_if_page_exist(self):
        response=self.client.get("/message/")
        self.assertEqual(response.status_code,200)
        
