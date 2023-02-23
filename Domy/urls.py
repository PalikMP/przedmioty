from .views import lista_domow
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.lista_domow, name='lista_domow'),
]