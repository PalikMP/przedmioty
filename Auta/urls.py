from django.urls import path, include
from . import views
from .views import lista_aut, auta_search
from django.conf import settings

urlpatterns = [
    path('', views.lista_aut, name='lista_aut'),
    path('search/', views.auta_search, name='auta_search'),
    ]