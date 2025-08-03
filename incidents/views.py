from django.db.models import Q
def search_incidents(request):
    incidents = Incident.objects.all()
    friend_name = request.GET.get('friend_name', '').strip()
    clumsy_level = request.GET.get('clumsy_level', '')
    if friend_name:
        incidents = incidents.filter(friend_name__icontains=friend_name)
    if clumsy_level:
        incidents = incidents.filter(clumsy_level=clumsy_level)
    incidents = incidents.order_by('-date')
    return render(request, 'incidents/search.html', {'incidents': incidents})

from django.shortcuts import render, redirect
from .models import Incident
from django import forms

class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['friend_name', 'description', 'clumsy_level']

def home(request):
    incidents = Incident.objects.order_by('-date')[:10]
    return render(request, 'incidents/home.html', {'incidents': incidents})

def add_incident(request):
    if request.method == 'POST':
        form = IncidentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = IncidentForm()
    return render(request, 'incidents/add_incident.html', {'form': form})
