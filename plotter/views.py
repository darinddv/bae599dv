from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
from .utils import chart1

# Create your views here.
def index(request):
    # return response sent from Django -> Browser
    return HttpResponse("This works") # Pass response as argument here

def your_handler(request):
    z = [1, 2, 3, 4]
    return render(request, 'plotter/plotter.html', {'z': z})

def plotter(request):
    return render(request, "plotter/plotter.html",context={'plot_div': chart1.plot_func()}) # Pass response as argument here
