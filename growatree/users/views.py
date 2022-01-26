from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .forms import UserRegisterForm
from recyclinghistory.models import RecyclingEntry


def register(request):
	"""
	Creates a User Registration Form
	"""
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Account created successfully! You can now log in.')
			return redirect('login')
	else:
		form = UserRegisterForm()
	return render(request, 'users/register.html', {'form': form, 'title': 'Register'})

@login_required
def profile(request):
	"""
	Displays User Profile Page
	"""
	totalWeight = RecyclingEntry.objects.filter(user__username= request.user.username).aggregate(Sum('recyclingWeight'))['recyclingWeight__sum']

	def chooseImage(treeSize):
		if treeSize == 0:
			return 0
		elif treeSize < 5:
			return 1
		elif treeSize < 10:
			return 5
		elif treeSize < 15:
			return 10
		elif treeSize <25:
			return 15
		elif treeSize < 50:
			return 25
		elif treeSize < 75:
			return 50
		elif treeSize < 90:
			return 75
		elif treeSize < 100:
			return 90
		elif treeSize < 125:
			return 100
		elif treeSize < 150:
			return 125
		return 150

	if totalWeight == None:
		tree = 0
	else:
		tree = totalWeight / 10

	context = {
		'tree' : tree,
		'image' : chooseImage(tree)
	}

	return render(request, 'users/profile.html', context)
