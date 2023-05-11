from django.urls import path
from . import views

urlpatterns = [
    #path('', views.ProductoDetail, name='ProductoDetail'),
    path('products/', views.ProductoList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductoDetail.as_view(), name='product-detail'),
]