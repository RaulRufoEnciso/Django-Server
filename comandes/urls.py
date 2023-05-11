from django.urls import path
from . import views

urlpatterns = [
     path('comandas', views.show_comandas.as_view(), name="show-comanda"),
     path('comandas/<int:pk>/', views.show_comandas.as_view(), name="show-comanda")
    
]