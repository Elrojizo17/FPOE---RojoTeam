from django.db import models
class Moto(models.Model):
	marca				= models.TextField(max_length=5000, null=False, blank=True)
	cilindraje			= models.IntegerField(null=False)
	modelo 				= models.IntegerField(null=False)
	color 				= models.TextField(max_length=5000, null=False, blank=True)
		
	def __str__(self):
		return self.marca