from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import SearchForm, SearchForm2
from django.db.models import Count
from django.shortcuts import render
from .models import Auta
from django.contrib.postgres.search import SearchVector


from .forms import SearchForm
from django.contrib.postgres.search import SearchVector

def lista_aut(request):
    lista_aut = Auta.objects.all()
    return render(request, 'lista_aut.html', {'lista_aut': lista_aut})

#----- SZUKANIE-- SZUKANIE-- SZUKANIE-- SZUKANIE-- SZUKANIE-- SZUKANIE-- SZUKANIE-- SZUKANIE-- SZUKANIE
def auta_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Auta.objects.annotate(search=SearchVector('kogo','opis'),).filter(search=query)
    return render(request, 'search.html',{'form':form, 'query':query, 'results':results})