from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import RecyclingHistory, RecyclingCreateView

class RecyclingHistoryTestUrls(SimpleTestCase):

    def test_recycling_history_url_resolves(self):
        url = reverse('recycling-history')
        self.assertEquals(resolve(url).func, RecyclingHistory)

    def test_add_recycling_entry_url_resolves(self):
        url = reverse('recyclingentry_create')
        self.assertEquals(resolve(url).func.view_class, RecyclingCreateView)