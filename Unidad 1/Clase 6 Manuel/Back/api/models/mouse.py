from django.db import models

class Mouse(models.Model):
    marca = models.CharField(max_length=50, null=False, blank=True)
    sensor = models.TextField(max_length=5000, null=False, blank=True)
    numbotones = models.IntegerField(null=False)  # Cambiado a IntegerField
    dpi = models.FloatField(null=False, blank=True)  # No está en blanco, asumo que puede ser opcional
    def __str__(self):
        return self.marca