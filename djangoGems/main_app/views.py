from django.shortcuts import render
from .models import Gem

# Create your views here.

# MSK: HttpResponse is not in use anymore, so we don't need its import either.
# from django.http import HttpResponse

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def gems_index(request):
  gems = Gem.objects.all()
  return render(request, 'gems/index.html', { 'gems': gems })    