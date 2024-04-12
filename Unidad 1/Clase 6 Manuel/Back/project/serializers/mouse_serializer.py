from rest_framework import serializers
from api.models.mouse import Mouse
class MouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mouse  
        exclude= ['id']