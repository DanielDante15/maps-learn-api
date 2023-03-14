from rest_framework import serializers
from .models import *


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['cep','logradouro','complemento','bairro','localidade','uf','num_casa']

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = ['razao_social','email','endereco','cnpj']

    def create(self, validated_data):
        user = Empresa.objects.create_superuser(
                  
        )

        return user


class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['nome','email','cpf','contato','endereco']

class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = ['num_doc','itens','volume','cliente','redespacho','end_redespacho']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['razao_social','endereco','lat','lng']