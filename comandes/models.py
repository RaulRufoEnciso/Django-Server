from django.db import models


class Comanda(models.Model):
    ESTAT_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    )

# usamos el método choices para poder escoger el tipo de estado del oedido
    estat = models.CharField(max_length=20, choices=ESTAT_CHOICES, default='pendiente')


