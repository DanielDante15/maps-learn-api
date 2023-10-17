from django.urls import path, include
from .views import *

from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('enderecos', EnderecoAPIView, basename='enderecos')
router.register('empresas', EmpresaAPIView, basename='empresas')
router.register('motoristas', MotoristaAPIView, basename='motoristas')
router.register('notas_fiscais', NotaFiscalAPIView, basename='notas_fiscais')
router.register('clientes', ClienteAPIView, basename='clientes')
router.register('entregas', EntregaAPIView, basename='entregas')
urlpatterns = router.urls