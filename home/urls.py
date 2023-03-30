from django.urls import path, include
from .views import *
from rest_framework import serializers, viewsets
from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('enderecos', EnderecoAPIView, basename='enderecos')
router.register('empresas', EmpresaAPIView, basename='empresas')
router.register('motoristas', MotoristaAPIView, basename='motoristas')
router.register('notas_fiscais', NotaFiscalAPIView, basename='notas_fiscais')
router.register('clientes', ClienteAPIView, basename='clientes')
urlpatterns = [
    path('clientes/',Clientes2.as_view(),name='clientes'),
    path('clientes/<int:pk>/',Clientes2.as_view(),name='clientes')
]