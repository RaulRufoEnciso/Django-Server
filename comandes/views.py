from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

@api_view(['GET'])
def getRuta(request):
    # Crear una respuesta HTTP

    list = [
        {'HOLA':'comanda'},
        {'HOLA1':'COOMANDA2'},
        {'HOLA2':'ADIOS2'},
    ]
    return Response(list)