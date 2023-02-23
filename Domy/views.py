from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Domy

def lista_domow(request):
    lista_domow = Domy.objects.all()
    return render(request, 'lista_domow.html', {'lista_domow': lista_domow})