from django.shortcuts import render

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