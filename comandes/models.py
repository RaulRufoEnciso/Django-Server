from django.db import models



class Comanda(models.Model):
    ESTAT_CHOICES = (
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    )
    comanda_id = models.CharField(max_length=10, primary_key=True)
    historial_comandes = models.CharField(max_length=30)
    estat = models.CharField(max_length=20, choices=ESTAT_CHOICES, default='pendiente')

