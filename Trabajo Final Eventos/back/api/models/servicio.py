from django.db import models
class Servicio(models.Model):
	nombre_servicio				= models.TextField(max_length=50, null=False, blank=True)
	cedula_cliente				= models.IntegerField(null=False)
	descripcion					= models.TextField(max_length=5000, null=False, blank=True)
	valor 						= models.TextField(max_length=5000, null=False, blank=True)

		
	def __str__(self):
		return self.nombre_servicio