from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import TreeInterface

class TreeInterfaceTestUrls(SimpleTestCase):

    def test_tree_interface_url_resolves(self):
        url = reverse('tree-interface')
        self.assertEquals(resolve(url).func, TreeInterface)