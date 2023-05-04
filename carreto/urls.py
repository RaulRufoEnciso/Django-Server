from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRuta, name='index'),

]