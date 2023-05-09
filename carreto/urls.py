from django.urls import path
from . import views

urlpatterns = [
    path('getRutas/', views.getRuta, name='getRutas'),
    path('getRutas2/', views.getRuta2, name='getRutas2'),

]