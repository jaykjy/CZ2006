from django.contrib import admin
from .models import RecyclingEntry


class RecyclingEntryAdmin(admin.ModelAdmin):
	"""
	Creates a Recycling Entry Model
	"""
	list_display = ('user', 'date', 'location', 'recyclingType', 'recyclingWeight')


admin.site.register(RecyclingEntry, RecyclingEntryAdmin)