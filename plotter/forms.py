from django import forms

class Locations(forms.Form):
    location = forms.CharField(label='Location', max_length=100)