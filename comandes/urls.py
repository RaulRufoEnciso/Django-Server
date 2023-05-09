from django.urls import path
from . import views

urlpatterns = [
     path('comanda', views.getRuta, name='index'),
     path('comandas', views.listar_comandas(), name='comandas'),


]