from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render

from .models import Frog

# Create your views here.
from django.shortcuts import render

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def frogs_index(request):
    frogs = Frog.objects.all() # Retrieve all frogs
    return render(request, 'frogs/index.html', 
    { 
        'frogs': frogs  #frogs on the page = the value of this key
    }
)

def frogs_detail(request, frog_id):
  frog = Frog.objects.get(id=frog_id)
  return render(request, 'frogs/detail.html', { 'frog': frog }) #frog is the variable we pass to page


# we import createview, updateview and delete view at the top
# imports out-of-the-box CRUD functionality

class FrogCreate(CreateView):
  model = Frog
  fields = '__all__' #all fields of model frog

class FrogUpdate(UpdateView):
  model = Frog
  fields = ['breed', 'description', 'age'] #fields offered on the page from model

class FrogDelete(DeleteView):
  model = Frog
  success_url = '/frogs' 
