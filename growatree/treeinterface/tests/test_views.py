from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class TreeInterfaceTestViews(TestCase):
    def setUp(self):
        # Create user
        test_user1 = User.objects.create_user(username='testuser1', password='(jnFe42i')
        test_user1.save()
        
        self.client = Client()
        self.tree_interface_url = reverse('tree-interface')

    def test_tree_interface_GET(self):
        login = self.client.login(username='testuser1', password='(jnFe42i')
        response = self.client.get(self.tree_interface_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'treeinterface/treeinterface.html')