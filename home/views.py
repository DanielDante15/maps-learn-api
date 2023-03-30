from django.shortcuts import render
from rest_framework.viewsets import *
from rest_framework.viewsets import *
from rest_framework import response, permissions,status
from rest_framework.decorators import api_view
from rest_framework_nested import routers
from .serializers import *


class EnderecoAPIView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer


class MotoristaAPIView(ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

class ClienteAPIView(RetrieveUpdateDestroyAPIView ):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def destroy(self, request, *args, **kwargs):
        
        print("*" * 50)
        return super().destroy(request, *args, **kwargs)

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
    
    

