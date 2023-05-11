'''
from django.shortcuts import render, redirect
from rest_framework import  generics
from .models import Producto
from .serializers import ProductoSerializer
'''

from rest_framework import generics
from .models import Producto
from .serializer import ProductoSerializer
#from django.http import HttpResponse

# Create your views here.


class ProductoList(generics.ListCreateAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

class ProductoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



#
#@api_view(['GET'])
#def show_all_products(request):
    #data =

