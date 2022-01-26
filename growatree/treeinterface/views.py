from django.shortcuts import render


def TreeInterface(request):
	"""
	Renders the Tree Interface
	"""
	return render(request, 'treeinterface/treeinterface.html')