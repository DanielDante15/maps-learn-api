from django.shortcuts import render
from rest_framework.viewsets import *
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

import googlemaps
import json
from django.conf import settings



class EnderecoAPIView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer

    def get_queryset(self):
        queryset = Endereco.objects.all()
        cliente_uid = self.request.query_params.get('cliente')
        print(cliente_uid)
        print("caiu aqui")
        if cliente_uid:
            queryset = queryset.filter(cliente = cliente_uid)
        return queryset
        

    def create(self, request, *args, **kwargs):

        rua = request.POST.get('logradouro')
        bairro = request.POST.get('bairro')
        num = request.POST.get('num_casa')
        cidade = request.POST.get('localidade')
        estado = request.POST.get('uf')
        gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
        result = json.dumps(gmaps.geocode(str(f'{rua},{num} {bairro} {cidade}-{estado}')))
        result2 = json.loads(result)
        cep = result2[0]['address_components'][6]['short_name']
        rua = result2[0]['address_components'][1]['long_name']
        bairro = result2[0]['address_components'][2]['long_name']
        cidade = result2[0]['address_components'][3]['long_name']
        estado = result2[0]['address_components'][4]['long_name']
        num = result2[0]['address_components'][0]['long_name']
        lat = result2[0]['geometry']['location']['lat']
        lng = result2[0]['geometry']['location']['lng']
        


        data={
            "cep":cep,
            "logradouro":rua,
            "bairro":bairro,
            "localidade":cidade,
            "uf":estado,
            "num_casa":num,
            "cliente":request.POST.get('cliente'),
            "latitude":lat,
            "longitude":lng,
        }

        serializer = self.serializer_class(data=data, # or request.data
                                                                        )
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


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


    
class EntregaAPIView(ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer


    