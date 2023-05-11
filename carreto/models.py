
from django.db import models
from cataleg.models import Producto

class Carreto(models.Model):
    product = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    estado = models.BooleanField()


