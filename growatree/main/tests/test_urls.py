from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import map

class MainTestUrls(SimpleTestCase):

    def test_map_url_resolves(self):
        url = reverse('map')
        self.assertEquals(resolve(url).func, map)

    