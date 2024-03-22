from rest_framework import serializers
from api.models import Post
from api.models import Mouse
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified']

class MouseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mouse  