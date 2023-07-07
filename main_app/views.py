from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Frog

# Create your views here.
from django.shortcuts import render

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

# def frogs_index(request):
#   # We pass data to a template very much like we did in Express!
#   return render(request, 'frogs/index.html', {
#     'frogs': frogs
#   })

def frogs_index(request):
    frogs = Frog.objects.all() # Retrieve all frogs
    return render(request, 'frogs/index.html', 
    { 
        'frogs': frogs 
    }
)

def frogs_detail(request, frog_id):
  frog = Frog.objects.get(id=frog_id)
  return render(request, 'frogs/detail.html', { 'frog': frog })

class FrogCreate(CreateView):
  model = Frog
  fields = '__all__'
  # success_url = '/frogs/{frog_id}'

class FrogUpdate(UpdateView):
  model = Frog
  fields = ['breed', 'description', 'age']

class FrogDelete(DeleteView):
  model = Frog
  success_url = '/frogs'