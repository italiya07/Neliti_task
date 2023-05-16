from django import forms
from django.core.validators import FileExtensionValidator
from django.forms import ModelForm

class SearchForm(forms.Form):
    latitude = forms.FloatField(label='Latitude', min_value=-90, max_value=90)
    longitude = forms.FloatField(label='Longitude', min_value=-180, max_value=180)