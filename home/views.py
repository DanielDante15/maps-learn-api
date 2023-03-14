from django.shortcuts import render
from rest_framework.viewsets import *
from rest_framework import response, permissions

from rest_framework_nested import routers
from .serializers import *


# class ClienteAPIView(ModelViewSet):
#     permission_classes = (permissions.IsAuthenticated, )
#     def get(self, request):
#         user = request.user
#         serializer = ClienteSerializer(user)
        
#         return response.Response({'user': serializer.data})
    
class EnderecoAPIView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

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
    
    

