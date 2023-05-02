from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

producto = {
            'name': 'silla',
            'descripcion': 'silla de plastico para jardin super resistente',
            'precio': '20€',
        }

def indexCataleg(request):

    return HttpResponse ("Hello, world")


