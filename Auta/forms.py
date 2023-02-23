from django.forms import ModelForm
from .models import Auta
from django import forms

class SearchForm(forms.Form):
    query = forms.CharField()

class SearchForm2(forms.Form):
    query = forms.CharField()