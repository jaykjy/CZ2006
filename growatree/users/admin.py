from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
	"""
	Creates an Admin Model
	"""
	list_display = ('user', 'image')


admin.site.register(Profile, ProfileAdmin)
