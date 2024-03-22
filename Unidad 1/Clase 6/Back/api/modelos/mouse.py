from django.db import models

class Mouse():
	marca = models.CharField()
	sensor = models.TextField()
	num_botones = models.IntegerField()
	dpi = models.IntegerField()
	def __str__(self):
		return self.marca