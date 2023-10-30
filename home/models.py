from uuid import uuid4
from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")

        return self.create_user(email=email, password=password, **extra_fields)

class Cliente(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid4)
    razao_social = models.CharField(max_length=50)

    def __str__(self):
        return (f'{self.razao_social}')
    
class Endereco(models.Model):
    cep = models.CharField(max_length=12, verbose_name='CEP',null=True)
    logradouro = models.CharField(max_length=50, verbose_name="Logradouro")
    complemento = models.CharField(max_length=50, verbose_name="Compemento",null=True,default='',blank=True)
    bairro = models.CharField(max_length=50, verbose_name="Bairro")
    localidade = models.CharField(max_length=20, verbose_name="Localidade")
    uf = models.CharField(max_length=20, verbose_name="UF")
    num_casa = models.CharField(max_length=6,verbose_name="Número",null=True,blank=True)
    latitude = models.FloatField(max_length=20,null=True,default=None)
    longitude = models.FloatField(max_length=20,null=True,default=None)
    cliente = models.ForeignKey(Cliente,verbose_name="Cliente",on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.logradouro}, {self.num_casa}, {self.bairro}, {self.localidade}"
    
class Motorista(models.Model):
    GEN_MASCULINO = 'M'
    GEN_FEMININO = 'F'

    GEN = [
        (GEN_FEMININO,'Feminino'),
        (GEN_MASCULINO,'Masculino'),
    ]
    nome = models.CharField(max_length=50, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    contato = models.CharField(max_length=15, verbose_name="Contato")
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, verbose_name="Endereço")
    entrega = models.ManyToManyField(Endereco,related_name='enderecos_entrega',blank=True,null=True)
    def __str__(self):
        return self.nome
    

class Empresa(AbstractUser):
    razao_social = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=80, unique=True)
    endereco = models.ForeignKey(Endereco, on_delete=models.PROTECT, verbose_name="Endereço",null=True)
    cnpj = models.CharField(max_length=18, unique=True)
    motorista = models.ManyToManyField(Motorista,related_name='lista_empresas',blank=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "cnpj"
    REQUIRED_FIELDS = ["razao_social", "email", "password"]

    def __str__(self):
        return (f'{self.razao_social}')
    

    def number(self):
        cnpj = self.cnpj.replace('.','').replace('/','').replace('-','')
        return cnpj


class NotaFiscal(models.Model):
    num_doc = models.CharField(max_length=50, verbose_name="Numero Documento")
    itens = models.IntegerField( verbose_name="Itens")
    volume = models.IntegerField(verbose_name="Volume")
    redespacho = models.BooleanField()
    end_redespacho = models.ForeignKey(Endereco,null=True, on_delete=models.PROTECT, verbose_name="Endereço")

    def __str__(self):

        return self.num_doc
    
