from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from api.models.cliente import  Cliente  
#from ..serializers.post_serializer import MotoSerializers
from project.serializers.clienteSerializer import ClienteSerializers


    

class Cliente_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        cliente = Cliente.objects.all()
        serializer = ClienteSerializers(cliente, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ClienteSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Cliente_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        Cliente = self.get_object(pk)
        serializer = ClienteSerializers(Cliente)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        Cliente = self.get_object(pk)
        serializer = ClienteSerializers(Cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        Cliente = self.get_object(pk)
        Cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)