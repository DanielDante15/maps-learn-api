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
    path('motoristas/<int:motorista_id>/entregas/', ListaEntregaMotoristaView.as_view(), name='motorista-entregas'),
    path('area-entrega/', AreaEntregaAPIView.as_view(), name='area-entrega'),
    path('area-entrega/<int:entrega_id>/', AreaEntregaAPIView.as_view(), name='area-entrega-detail'),
]

