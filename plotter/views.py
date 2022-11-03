from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string
import pandas as pd
from .utils import chart1
from .models import LocationLoadsTables
# Create your views here.
def index(request):
    # return response sent from Django -> Browser
    return HttpResponse("This works") # Pass response as argument here

def your_handler(request):
    z = [1, 2, 3, 4]
    return render(request, 'plotter/plotter.html', {'z': z})

#def plotter(request):
#    batteries = LocationLoadsTables.batteries
#    loads = LocationLoadsTables.loads
#    json_to_df = pd.read_json()
#    return render(request, "plotter/plotter.html",context={'plot_div': chart1.plot_func(json_to_df)}) # Pass response as argument here
