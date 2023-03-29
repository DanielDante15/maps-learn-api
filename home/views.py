from django.shortcuts import render
from rest_framework.viewsets import *
from rest_framework import response, permissions,status
from rest_framework.decorators import api_view
from rest_framework_nested import routers
from .serializers import *


class EnderecoAPIView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    @api_view(['GET','PUT','DELETE'])
    def endereco_detail(request,pk):
        try:
            endereco = Endereco.objects.get(pk=pk)
        except Endereco.DoesNotExist:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
        
        if request.method == 'GET':
            serializer = EnderecoSerializer(endereco)
            return response.Response(serializer.data)
        elif request.method == 'PUT':
            serializer = EnderecoSerializer(endereco,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return response.Response(serializer.data)
            return response.Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            endereco.delete()
            return response.Response(status=status.HTTP_204_NO_CONTENT)









class MotoristaAPIView(ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

class ClienteAPIView(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class NotaFiscalAPIView(ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer



class EmpresaAPIView(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

    # def get(self, request):
    #     user = request.user
    #     print(request.user)
    #     serializer = EmpresaSerializer(user)
        
    #     return response.Response({'endereco': serializer.data})
    
    

