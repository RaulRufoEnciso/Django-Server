from django.urls import path
from . import views

urlpatterns = [
    path('getRutas/', views.getRuta, name='getRutas'),
    path('productos/<str:pk>/', views.getProducts, name='getProducts'),
    path('postProductos/<str:pk>/', views.postProducts, name='getProducts'),
]