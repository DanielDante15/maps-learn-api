from rest_framework import serializers
from .models import *


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = "__all__"


class EmpresaSerializer(serializers.ModelSerializer):
    endereco = serializers.CharField(source='endereco.logradouro',read_only=True)
    class Meta:
        model = Empresa 
        fields = '__all__'

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = ['id','username','email','password','cpf','contato','endereco','entrega']
    def create(self, validated_data):
        user = Motorista(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class NotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotaFiscal
        fields = ['num_doc','itens','volume','redespacho','end_redespacho']

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id','razao_social']
        read_only_fields = [('id')]

class EntregaMotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = ['id', 'cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'num_casa', 'latitude', 'longitude', 'cliente']

