from rest_framework import serializers
from api.models.moto import Moto

class MotoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moto  
        exclude = ['id'] 