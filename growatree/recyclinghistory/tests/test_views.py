from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from ..models import RecyclingEntry


class RecyclingHistoryTestView(TestCase):

    def setUp(self):
        # Create test user
        test_user1 = User.objects.create_user(username='testuser1', password='(jnFe42i')
        test_user1.save()

        # Initialise Client, urls and models to test
        self.client = Client()
        self.recycling_history_url = reverse('recycling-history')
        self.recyclingentry_create_url = reverse('recyclingentry_create')
        self.RecyclingEntry1 = RecyclingEntry.objects.create(
            user=test_user1,
            date=timezone.now(),
            location='NTU',
            recyclingType='Plastic',
            recyclingWeight=10
        )
      
    def test_logged_in_recyling_history_GET(self):
        login = self.client.login(username='testuser1', password='(jnFe42i')
        response = self.client.get(self.recycling_history_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recyclinghistory/recyclinghistory.html')

    def test_logged_in_create_recyling_entry_GET(self):
        login = self.client.login(username='testuser1', password='(jnFe42i')
        response = self.client.get(self.recyclingentry_create_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'recyclinghistory/recyclingentry_form.html')

    def test_created_recyling_entry_POST(self):
        response = self.client.post(self.recyclingentry_create_url, {
            'recyclingType': 'Plastic',
            'recyclingWeight': 10
        })

        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.RecyclingEntry1.recyclingType, 'Plastic')
        self.assertEquals(self.RecyclingEntry1.recyclingWeight, 10)


# TODO
# class UpdateLocationTestView(TestCase):
#     def test_update_location_GET(self):
#         response = self.client.get(reverse('update_location'))
#         self.assertEqual(response.status_code, 200)
