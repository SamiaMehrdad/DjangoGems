from django.shortcuts import render
from .models import Gem, gems

# Create your views here.
# Add the following import
from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gems_index(request):
  return render(request, 'gems/index.html', { 'gems': gems })    