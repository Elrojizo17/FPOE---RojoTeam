from django.db import models
class Cliente(models.Model):
	nombre				= models.TextField(max_length=50, null=False, blank=True)
	apellido			= models.TextField(max_length=5000, null=False, blank=True)
	cedula 				= models.IntegerField(null=False)
	telefono 			= models.IntegerField(null=False)
	correo			    = models.TextField(max_length=5000, null=False, blank=True)
		
	def __str__(self):
		return self.nombre