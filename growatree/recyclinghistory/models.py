from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class RecyclingEntry(models.Model):
	"""
	Creates a Recycling Entry Model
	"""
	user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
	date = models.DateTimeField(default=timezone.now)
	location = models.TextField(default="NTU")
	recyclingType = models.TextField()
	recyclingWeight = models.PositiveSmallIntegerField()
	
	def get_absolute_url(self):
		return reverse('recycling-history')
	
	def __str__(self):
		return self.recyclingType 

	class Meta:
		ordering = ["-date"]
