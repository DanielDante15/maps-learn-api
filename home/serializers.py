from rest_framework import serializers
from .models import *


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id','cep','logradouro','complemento','bairro','localidade','uf','num_casa']


class EmpresaSerializer(serializers.ModelSerializer):
    endereco = serializers.CharField(source='endereco.logradouro',read_only=True)
    motorista = serializers.PrimaryKeyRelatedField(queryset=Motorista.objects.all(), many=True)
    class Meta:
        model = Empresa
        fields = ['razao_social','email','endereco','cnpj','username','password','motorista']

class EmpresaRelatedField(serializers.RelatedField):
    def to_internal_value(self, data):
        return Empresa.objects.get(name=data)

class MotoristaSerializer(serializers.ModelSerializer):
    endereco = serializers.CharField(source='endereco.logradouro',read_only=True)
    lista_empresas = serializers.PrimaryKeyRelatedField(queryset=Empresa.objects.filter(), many=True)
    class Meta: 
        model = Motorista
        fields = ['nome','email','cpf','contato','endereco','lista_empresas']

class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = ['num_doc','itens','volume','cliente','redespacho','end_redespacho']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['razao_social','endereco','lat','lng']