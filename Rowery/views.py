from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Rowery

def lista_rowerow(request):
    lista_rowerow = Rowery.objects.all()
    return render(request, 'lista_rowerow.html', {'lista_rowerow': lista_rowerow})
