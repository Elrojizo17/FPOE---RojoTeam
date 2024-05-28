from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from api.models.cliente import Cliente
from project.serializers.clienteSerializer import ClienteSerializers

class Cliente_APIView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = Cliente.objects.all()
        nombre = request.query_params.get('nombre')
        apellido = request.query_params.get('apellido')
        cedula = request.query_params.get('cedula')
        telefono = request.query_params.get('telefono')
        correo = request.query_params.get('correo')

        if nombre is not None:
            queryset = queryset.filter(nombre=nombre)
        if apellido is not None:
            queryset = queryset.filter(apellido=apellido)
        if cedula is not None:
            queryset = queryset.filter(cedula=cedula)
        if telefono is not None:
            queryset = queryset.filter(telefono=telefono)
        if correo is not None:
            queryset = queryset.filter(correo=correo)

        serializer = ClienteSerializers(queryset, many=True)
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
        cliente = self.get_object(pk)
        serializer = ClienteSerializers(cliente)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cliente = self.get_object(pk)
        serializer = ClienteSerializers(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cliente = self.get_object(pk)
        cliente.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
