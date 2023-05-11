#from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .models import Comanda
from django.core import serializers
from rest_framework import generics
from .serializer import comandasSerializer

# Create your views here.



class show_comandas(generics.ListCreateAPIView):
    queryset = Comanda.objects.all()
    serializer_class = comandasSerializer