from .views import lista_rowerow
from django.urls import path, include
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.lista_rowerow, name='lista_rowerow'),
]