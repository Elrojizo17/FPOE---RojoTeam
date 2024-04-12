from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from api.models.moto import Moto    
#from ..serializers.post_serializer import MotoSerializers
from project.serializers.moto_serializer import MotoSerializers


    

class Moto_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        moto = Moto.objects.all()
        serializer = MotoSerializers(moto, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = MotoSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Moto_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Moto.objects.get(pk=pk)
        except Moto.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        moto = self.get_object(pk)
        serializer = MotoSerializers(moto)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        moto = self.get_object(pk)
        serializer = MotoSerializers(moto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        moto = self.get_object(pk)
        moto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)