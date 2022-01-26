from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


def map(response):
    """
    Renders the Map HTML file
    """
    return render(response, "main/map.html", {})
    