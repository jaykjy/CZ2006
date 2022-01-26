from django.test import TestCase, Client
from django.urls import reverse

class MainTestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.map_url = reverse('map')

    def test_map_GET(self):
        response = self.client.get(self.map_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/map.html')