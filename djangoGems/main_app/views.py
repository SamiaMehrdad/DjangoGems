from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Gem
from .forms import FamousForm
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
  famous_form=FamousForm()
  return render(request, 'gems/detail.html', {
     'gem': gem,
     'famous_form': famous_form
      })  

def add_famous(request, gem_id):
    # create a ModelForm instance using the data in request.POST
  form = FamousForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_famous = form.save(commit=False)
    new_famous.gem_id = gem_id
    new_famous.save()
  return redirect('detail', gem_id=gem_id)

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