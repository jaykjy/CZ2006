from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView
from .models import RecyclingEntry


def RecyclingHistory(request):
	"""
	Queries all the Recycling Entires and renders the Recycling History Page
	"""
	context = {
		'database_info' : RecyclingEntry.objects.filter(user__username= request.user.username)
	}

	return render(request, 'recyclinghistory/recyclinghistory.html', context)

# TODO: Complete this!!!!!!!
def UpdateLocation(request):
	location = request.GET.get('location', None)
	request.session['location'] = location

	return HttpResponse('Location successfully updated!')


class RecyclingCreateView(LoginRequiredMixin, CreateView):
	"""
	Creates a Recycling Entry Form for user to Recycle
	"""
	model = RecyclingEntry
	fields = ['recyclingType', 'recyclingWeight']

	def form_valid(self, form):
		# Updates user to database
		form.instance.user = self.request.user

		# Update location to database
		form.instance.location = self.request.session.get('location', False)

		return super().form_valid(form)
