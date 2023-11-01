from django.urls import path, include
from .views import *

from rest_framework_nested import routers


router = routers.DefaultRouter()

router.register('endereco', EnderecoAPIView, basename='Endereço')
router.register('empresas', EmpresaAPIView, basename='Empresas')
router.register('motoristas', MotoristaAPIView, basename='Motoristas')
router.register('notas_fiscais', NotaFiscalAPIView, basename='Notas Fiscais')
router.register('clientes', ClienteAPIView, basename='Clientes')
urlpatterns = [
    path('',include(router.urls)),
    path('motoristas/<int:motorista_id>/entregas/', ListaEntregaMotoristaView.as_view(), name='motorista-entregas'),
    path('endereco/entregas', AreaEntregaAPIView.as_view(), name='area-entrega'),
    path('endereco/<int:entrega_id>/entregas/', AreaEntregaAPIView.as_view(), name='area-entrega-detail'),
    # path('login/', user_login, name='login'),
    # path('logout/', user_logout, name='logout'),
]

