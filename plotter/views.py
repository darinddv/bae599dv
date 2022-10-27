from django.shortcuts import render

from django.http import HttpResponse
from django.template.loader import render_to_string
# Create your views here.
def index(request):
    # return response sent from Django -> Browser
    return HttpResponse("This works") # Pass response as argument here

def plotter(request):
    # return response sent from Django -> Browser
    return render(request, "plotter/plotter.html") # Pass response as argument here
