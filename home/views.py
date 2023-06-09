from django.shortcuts import render
from rest_framework.viewsets import *
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *


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
    
    

