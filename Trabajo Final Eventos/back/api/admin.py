from django.contrib import admin
from .models.cliente import Cliente
from .models.servicio import Servicio

admin.site.register(Cliente)
admin.site.register(Servicio)