from rest_framework.viewsets import *
from rest_framework.status import *
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from rest_framework.views import APIView
import googlemaps
import numpy as np
import json
from django.conf import settings



class EnderecoAPIView(ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Endereco.objects.all()
        cliente_uid = self.request.query_params.get('cliente')
        if cliente_uid:
            queryset = queryset.filter(cliente = cliente_uid)
        return queryset
        

    def create(self, request, *args, **kwargs):
        if request.POST.get('latitude') == '' and request.POST.get('longitude') == '':
            rua = request.POST.get('logradouro')
            bairro = request.POST.get('bairro')
            num = request.POST.get('num_casa')
            cidade = request.POST.get('localidade')
            estado = request.POST.get('uf')

            gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
            result = json.dumps(gmaps.geocode(str(f'{rua},{num} {bairro} {cidade}-{estado}')))
            result2 = json.loads(result)
            data = result2[0]

            print(data['address_components'])
            print(len(data['address_components']))

            if len(data['address_components']) == 6:
                cep = data['address_components'][5]['short_name']
                rua = data['address_components'][0]['long_name']
                bairro = data['address_components'][1]['long_name']
                cidade = data['address_components'][2]['long_name']
                estado = data['address_components'][3]['short_name']
                lat = data['geometry']['location']['lat']
                lng = data['geometry']['location']['lng']
            else:
                cep = data['address_components'][6]['short_name']
                rua = data['address_components'][1]['long_name']
                bairro = data['address_components'][2]['long_name']
                cidade = data['address_components'][3]['long_name']
                estado = data['address_components'][4]['short_name']
                lat = data['geometry']['location']['lat']
                lng = data['geometry']['location']['lng']


            
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

            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else:


            lat = request.POST.get('latitude')
            lng = request.POST.get('longitude')

            gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
            reverse_geocode_result = json.dumps(gmaps.reverse_geocode((lat, lng)))
            result = json.loads(reverse_geocode_result)
            data = result[0]

            print(len(data))

            num = data['address_components'][0]['short_name']
            cep = data['address_components'][6]['short_name']
            rua = data['address_components'][1]['long_name']
            bairro = data['address_components'][2]['long_name']
            cidade = data['address_components'][3]['long_name']
            estado = data['address_components'][4]['short_name']
            

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

            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            



            

    


class MotoristaAPIView(ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer

    def adicionar_endereco_a_motorista(self, request, pk):
        motorista = self.get_object()  # Obtém o objeto Motorista pelo ID (pk) da URL
        endereco_ids = request.data.get('endereco_ids', [])  # Supondo que você fornece uma lista de IDs de Endereco a serem adicionados

        try:
            enderecos = Endereco.objects.filter(id__in=endereco_ids)  # Obtém os objetos Endereco com base nos IDs fornecidos
            motorista.entrega.set(enderecos)  # Usa o método .set() para adicionar os objetos Endereco ao campo Many-to-Many entrega
            return Response({'detail': 'Endereços adicionados com sucesso.'}, status=status.HTTP_200_OK)
        except Endereco.DoesNotExist:
            return Response({'detail': 'Um ou mais IDs de Endereco não existem.'}, status=status.HTTP_400_BAD_REQUEST)

class ClienteAPIView(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    


class NotaFiscalAPIView(ModelViewSet):
    queryset = NotaFiscal.objects.all()
    serializer_class = NotaFiscalSerializer



class EmpresaAPIView(ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ListaEntregaMotoristaView(APIView):
    def get(self, request, motorista_id):
        try:
            motorista = Motorista.objects.get(id=motorista_id)
        except Motorista.DoesNotExist:
            return Response({'detail': 'Motorista não encontrado.'}, status=status.HTTP_404_NOT_FOUND)

        entregas = motorista.entrega.all()  # Obtém todas as entregas relacionadas a esse motorista
        serializer = EntregaMotoristaSerializer(entregas, many=True)
        return Response(serializer.data)


class AreaEntregaAPIView(APIView):
    def get(self, request, entrega_id=None):
        gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
        coordenadas = []
        if entrega_id is not None:
            try:
                motorista = Motorista.objects.get(id=entrega_id)
                entregas = motorista.entrega.all()

                for entrega in entregas:
                    coordenadas.append(
                    (entrega.latitude,
                    entrega.longitude,)
                )
                
                esquerda = min(coordenadas, key=lambda p: p[0])
                direita = max(coordenadas, key=lambda p: p[0])
                acima = max(coordenadas, key=lambda p: p[1])
                abaixo = min(coordenadas, key=lambda p: p[1])

                centro_x = (esquerda[0] + direita[0]) / 2
                centro_y = (acima[1] + abaixo[1]) / 2

                centro = (centro_x,centro_y)

                distancias = [gmaps.distance_matrix(centro, ponto, mode="driving")["rows"][0]["elements"][0]["distance"]["value"] for ponto in coordenadas]

# O raio do círculo será a maior distância
                raio = max(distancias) / 1000

                return Response({'coordenadas': coordenadas,
                             'centroX': centro_x,
                             'centroY': centro_y,
                             'raio': raio}, status=status.HTTP_200_OK)
                    
            except Motorista.DoesNotExist:
                return Response({"error": "Motorista não encontrado"}, status=status.HTTP_404_NOT_FOUND)
        else:
            
            try:
                enderecos = Endereco.objects.all()
            except Endereco.DoesNotExist:
                return Response({'msg': 'Endereços não encontrados.'}, status=status.HTTP_404_NOT_FOUND)

            for endereco in enderecos:
                coordenadas.append(
                    (endereco.latitude,
                    endereco.longitude,)
                )

            esquerda = min(coordenadas, key=lambda p: p[0])
            direita = max(coordenadas, key=lambda p: p[0])
            acima = max(coordenadas, key=lambda p: p[1])
            abaixo = min(coordenadas, key=lambda p: p[1])

            centro_x = (esquerda[0] + direita[0]) / 2
            centro_y = (acima[1] + abaixo[1]) / 2

            centro = (centro_x,centro_y)

            distancias = [gmaps.distance_matrix(centro, ponto, mode="driving")["rows"][0]["elements"][0]["distance"]["value"] for ponto in coordenadas]

# O raio do círculo será a maior distância
            raio = max(distancias) / 1000

            return Response({'coordenadas': coordenadas,
                             'centroX': centro_x,
                             'centroY': centro_y,
                             'raio': raio}, status=status.HTTP_200_OK)

    
    



    