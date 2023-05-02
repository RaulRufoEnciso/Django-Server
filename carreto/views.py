from django.shortcuts import render, redirect

# Create your views here.

producto = {
            'name': 'silla',
            'descripcion': 'silla de plastico para jardin super resistente',
            'precio': '20€',
        }

def index(request):

    return render(request,'index.html', {'Nombre': producto['name'],
                                         'Descripcion': producto['descripcion'],
                                         'Precio': producto['precio']
                                        })

