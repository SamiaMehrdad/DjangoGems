from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

def gems_detail(request, gem_id):
  gem = Gem.objects.get(id=gem_id)
  return render(request, 'gems/detail.html', { 'gem': gem })  

class GemCreate(CreateView):
  model = Gem
  fields = '__all__'  
  success_url = '/gems/'

class GemUpdate(UpdateView):
  model = Gem
  # Let's disallow the renaming of a gem by excluding the name field!
  fields = ['theme', 'description', 'price_range', 'hardness']

class GemDelete(DeleteView):
  model = Gem
  success_url = '/gems/'  