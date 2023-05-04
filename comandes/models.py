from django.db import models


class Comanda(models.Model):
    ESTAT_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    )

# usamos el método choices para poder escoger el tipo de estado del oedido
    comanda_id = models.CharField(max_length=10, primary_key=True)
    estat = models.CharField(max_length=20, choices=ESTAT_CHOICES, default='pendiente')


class HistorialComandas(models.Model):
    comanda = models.ForeignKey(Comanda, on_delete=models.CASCADE)
    estat_comanda = models.CharField(max_length=20)