from rest_framework.response import Response
from rest_framework.views import APIView
from project.serializers.mouse_serializer import MouseSerializers
#from ..serializers import MouseSerializers
from api.models.mouse import Mouse
from rest_framework import status
from django.http import Http404

class Mouse_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        mouse = Mouse.objects.all()
        serializer = MouseSerializers(mouse, many=True)
        
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = MouseSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class Mouse_APIView_Detail(APIView):
    def get_object(self, pk):
        try:
            return Mouse.objects.get(pk=pk)
        except Mouse.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        mouse = self.get_object(pk)
        serializer = MouseSerializers(mouse)  
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        mouse = self.get_object(pk)
        serializer = MouseSerializers(mouse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        mouse = self.get_object(pk)
        mouse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)