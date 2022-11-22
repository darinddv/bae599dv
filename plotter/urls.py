from django.urls import path
from . import views

# List of supported URLs, and the View that should be triggered when 
# request for this URL is made
# This is a 'URLconf' (URL config)
urlpatterns = [
    # path("URL page", pointer-to-view)
    path("plotter", views.plotter),
    path("index2", views.index2),
    path("shapely", views.shapely)
]