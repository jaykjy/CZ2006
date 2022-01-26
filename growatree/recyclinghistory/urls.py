from django.urls import path
from . import views
from .views import RecyclingCreateView


urlpatterns = [
    path('', views.RecyclingHistory, name = 'recycling-history'),
    path('recyclingentry/new/', RecyclingCreateView.as_view(), name = 'recyclingentry_create'),
    path('update_location/', views.UpdateLocation, name = 'update_location'),
]