
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

# producto = {
#             'name': 'silla',
#             'descripcion': 'silla de plastico para jardin super resistente',
#             'precio': '20€',
#         }

# def index(request):
#
#     return render(request,'index.html', {'Nombre': producto['name'],
#                                          'Descripcion': producto['descripcion'],
#                                          'Precio': producto['precio']
#                                         })

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
@api_view(['POST','GET'])
def getRuta2(request):

    list = [
        {'HOLA':'ADIOS'},
        {'HOLA1':'ADIOS1'},
        {'HOLA2':'ADIOS2'},
    ]
    return Response(list)


