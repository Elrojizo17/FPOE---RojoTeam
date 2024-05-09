from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from api.models.servicio import  Servicio
from project.serializers.servicioSerializer import ServicioSerializers


    

class Servicio_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        servicio = Servicio.objects.all()
        serializer = ServicioSerializers(servicio, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = ServicioSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Servicio_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Servicio.objects.get(pk=pk)
        except Servicio.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        Servicio = self.get_object(pk)
        serializer = ServicioSerializers(Servicio)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        Cliente = self.get_object(pk)
        serializer = ServicioSerializers(Servicio, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        Servicio = self.get_object(pk)
        Servicio.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)