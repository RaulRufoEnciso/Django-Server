from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Carreto
from cataleg.models import Producto

# Crear la vista
@api_view(['GET'])
def getRuta(request):
    list = [
        {'HOLA':'ADIOS'},
        {'HOLA1':'ADIOS1'},
        {'HOLA2':'ADIOS2'},
    ]
    return Response(list)

# Objetos en el carreto

#Añadir productos a la tabla
@api_view(['GET','POST'])
def postProducts(request, pk):
    query = Producto.objects.get(id=pk)
    return Response(query)

#Obtener productos
@api_view(['GET'])
def getProducts(request, pk):

    products = Producto.objects.get(id=pk)
    context = {""}
    return Response(products);


