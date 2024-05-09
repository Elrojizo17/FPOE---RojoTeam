from rest_framework import serializers
from api.models.servicio import Servicio

class ServicioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Servicio 