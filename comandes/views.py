from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse


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



def actualizar_estado_pedido(request, comanda_id):
    comanda = get_object_or_404(comanda, pk=comanda_id)
    # falta definir los atributos del objeto comanda en el modelo de la app comandes
    comanda.estat = 'pagado'
    comanda.save()
    return JsonResponse({'success': True})
