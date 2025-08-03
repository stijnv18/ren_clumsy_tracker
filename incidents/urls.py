from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_incident, name='add_incident'),
    path('search/', views.search_incidents, name='search_incidents'),
]
