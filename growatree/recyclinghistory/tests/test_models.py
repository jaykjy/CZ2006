from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from ..models import RecyclingEntry


class RecyclingHistoryTestModels(TestCase):

    def setUp(self):
        # Create test user
        test_user1 = User.objects.create_user(username='testuser1', password='(jnFe42i')
        test_user1.save()
        
        self.RecyclingEntry1 = RecyclingEntry.objects.create(
            user=test_user1,
            date=timezone.now(),
            location='NTU',
            recyclingType='Plastic',
            recyclingWeight=10
        )
    
    def test_recycling_entry_str_is_equal_to_recycling_type(self):
        self.assertEqual(str(self.RecyclingEntry1), self.RecyclingEntry1.recyclingType)