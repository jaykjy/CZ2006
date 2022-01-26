from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from ..models import Profile

class UserTestViews(TestCase):
    def setUp(self):
        # Create user
        test_user1 = User.objects.create_user(username='testuser1', password='(jnFe42i')
        test_user1.save()
        
        self.client = Client()
        self.register_url = reverse('register')
        self.profile_url = reverse('profile')

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_profile_GET(self):
        login = self.client.login(username='testuser1', password='(jnFe42i')
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')