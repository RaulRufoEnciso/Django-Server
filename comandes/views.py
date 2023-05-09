#from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Comanda
from django.core import serializers


# Create your views here.

@api_view(['POST'])
def getRuta(request):
    # Crear una respuesta HTTP

    list = [
        {'HOLA':'comanda'},
        {'HOLA1':'COOMANDA2'},
        {'HOLA2':'ADIOS2'},
    ]
    return Response(list)

def listar_comandas(request):
    comandas = Comanda.objects.all()
    comandas_serialized = serializers.serialize('json', comandas)
    return JsonResponse(comandas_serialized, safe=False)
