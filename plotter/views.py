from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string

import pandas as pd

from .utils import chart1
from .utils import shapely_module
from .models import LocationLoadsTables
from .forms import Locations

# Create your views here.
def index(request):
    # return response sent from Django -> Browser
    return HttpResponse("This works") # Pass response as argument here

def your_handler(request):
    z = [1, 2, 3, 4]
    return render(request, 'plotter/plotter.html', {'z': z})

def plotter(request):
    #batteries = LocationLoadsTables.batteries
    #loads = LocationLoadsTables.loads
    #json_to_df = pd.read_json()
    return render(request, "plotter/plotter.html",context={'plot_div': chart1.plot_func()}) # Pass response as argument here

def index2(request):
    return render(request, "plotter/index2.html",context={'plot_div': chart1.plot_func()}) # Pass response as argument here

def shapely(request):
    return render(request, "plotter/shapely.html",context={'plot_div': shapely_module.polygon()}) # Pass response as argument here

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Locations(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Locations()

    return render(request, "plotter/index2.html", {'form': form})