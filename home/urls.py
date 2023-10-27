from django.urls import path, include
from .views import *

from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('enderecos', EnderecoAPIView, basename='Endereços')
router.register('empresas', EmpresaAPIView, basename='Empresas')
router.register('motoristas', MotoristaAPIView, basename='Motoristas')
router.register('notas_fiscais', NotaFiscalAPIView, basename='Notas Fiscais')
router.register('clientes', ClienteAPIView, basename='Clientes')
urlpatterns = [
    path('',include(router.urls)),
]